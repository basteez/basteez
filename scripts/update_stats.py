#!/usr/bin/env python3
"""Fetch GitHub stats for the profile and write them to assets/stats.json.

Uses only the standard library (urllib) so the CI job needs no extra deps.
Reads the token from $STATS_TOKEN (a PAT — gives private-inclusive numbers) or
falls back to $GH_TOKEN / $GITHUB_TOKEN (public-only numbers).

Run:
    STATS_TOKEN=ghp_xxx python3 scripts/update_stats.py
then regenerate the card with scripts/gen_neofetch.py.
"""
import json
import os
import sys
import urllib.request

LOGIN = "basteez"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "stats.json")

TOKEN = os.environ.get("STATS_TOKEN") or os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    sys.exit("No token in STATS_TOKEN / GH_TOKEN / GITHUB_TOKEN")

API = "https://api.github.com/graphql"


def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(API, data=body, method="POST")
    req.add_header("Authorization", f"bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", f"{LOGIN}-neofetch-stats")
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"], indent=2))
    return data["data"]


def fmt(n):
    return f"{n:,}"


def fetch():
    # profile + created date + contributed-to count
    base = gql(
        """
        query($login:String!) {
          user(login:$login) {
            createdAt
            followers { totalCount }
            repositories(privacy:PUBLIC, ownerAffiliations:OWNER) { totalCount }
            repositoriesContributedTo(
              includeUserRepositories:false,
              contributionTypes:[COMMIT, PULL_REQUEST, ISSUE, REPOSITORY]
            ) { totalCount }
          }
        }
        """,
        {"login": LOGIN},
    )["user"]

    followers = base["followers"]["totalCount"]
    repos = base["repositories"]["totalCount"]
    contributed = base["repositoriesContributedTo"]["totalCount"]
    created_year = int(base["createdAt"][:4])

    # total stars across all owned repos (paginate)
    stars = 0
    cursor = None
    while True:
        page = gql(
            """
            query($login:String!, $cursor:String) {
              user(login:$login) {
                repositories(first:100, ownerAffiliations:OWNER, after:$cursor) {
                  nodes { stargazerCount }
                  pageInfo { hasNextPage endCursor }
                }
              }
            }
            """,
            {"login": LOGIN, "cursor": cursor},
        )["user"]["repositories"]
        stars += sum(n["stargazerCount"] for n in page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]

    # lifetime commit contributions: sum per contribution year
    import datetime
    this_year = datetime.datetime.now(datetime.timezone.utc).year
    commits = 0
    for year in range(created_year, this_year + 1):
        frm = f"{year}-01-01T00:00:00Z"
        to = f"{year}-12-31T23:59:59Z"
        cc = gql(
            """
            query($login:String!, $from:DateTime!, $to:DateTime!) {
              user(login:$login) {
                contributionsCollection(from:$from, to:$to) {
                  totalCommitContributions
                  restrictedContributionsCount
                }
              }
            }
            """,
            {"login": LOGIN, "from": frm, "to": to},
        )["user"]["contributionsCollection"]
        commits += cc["totalCommitContributions"] + cc["restrictedContributionsCount"]

    return {
        "repos": fmt(repos),
        "stars": fmt(stars),
        "commits": fmt(commits),
        "contributed": fmt(contributed),
        "followers": fmt(followers),
    }


def main():
    stats = fetch()
    with open(OUT, "w") as f:
        json.dump(stats, f, indent=2)
        f.write("\n")
    print("wrote", OUT, stats)


if __name__ == "__main__":
    main()
