<!--
  EDITING GUIDE
  =============
  This README is themed as terminal / neofetch output. Owner-editable
  regions are bracketed by `EDIT:*` / `END:*` comment markers. Edit
  between the markers only; leave surrounding layout HTML untouched.

  - The neofetch hero card is a pair of self-hosted SVGs:
      assets/neofetch-dark.svg  +  assets/neofetch-light.svg
    Do NOT hand-edit the SVGs. To change the info fields/sections or the
    colors, edit scripts/gen_neofetch.py, then regenerate:
        python3 scripts/gen_neofetch.py
    (Serving from the repo means no third-party card service can rot.)
    - The ASCII portrait lives in assets/portrait.txt (one row per line).
      Regenerate it from a photo with a brightness→character ramp, or edit
      the text by hand.
    - The "GitHub Stats" numbers come from assets/stats.json, refreshed by
      scripts/update_stats.py via the "Refresh neofetch card stats" GitHub
      Action. Add a read-only PAT as the STATS_TOKEN repo secret for
      private-inclusive numbers; otherwise public-only stats are used.

  - EDIT:PROMPT-LINES     — Typed-command lines above the card
                            (readme-typing-svg). Keep the shell-prompt
                            style, e.g. "tiziano@bstz:~$ neofetch".
  - EDIT:ABOUT            — Plain-language About paragraph. ≤3 sentences.
  - EDIT:TECH-BADGES      — 3–9 shields.io badges, style=for-the-badge.
                            Each: valid simple-icons logo slug + alt text.
  - EDIT:FEATURED-PROJECTS — 2–6 curated projects, most-worth-seeing
                             first. `[name](url) — one-line description`.
  - EDIT:WRITING-LIST     — Hand-curated writing only. Series-clustered
                            items on one bullet with arrow-chain links.
  - EDIT:CONTACT-LINKS    — Contact/social badges in a single <p>.
                            Order: LinkedIn, dev.to, Stack Overflow, Email.

  Note: the neofetch card is a fully static image, so motion-sensitive
  readers get the whole profile from it plus the sections below.
-->

<p align="center">
  <!-- EDIT:PROMPT-LINES — Shell-prompt style. "$" is %24, " " is +, "·" is %C2%B7, "&" is %26. -->
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1500&color=3FB950&center=true&vCenter=true&width=640&lines=tiziano%40bstz%3A~%24+neofetch;Senior+Software+Engineer;Clean+code+%26+AI+enthusiast;Java+%C2%B7+Quarkus+%C2%B7+Spring+Boot+%C2%B7+Kubernetes;Writes+at+bstz.it"
    alt="tiziano@bstz:~$ neofetch — Senior Software Engineer · Clean code & AI enthusiast · Java · Quarkus · Spring Boot · Kubernetes · Writes at bstz.it"
  />
  <!-- END:PROMPT-LINES -->
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/neofetch-dark.svg?v=2" />
    <source media="(prefers-color-scheme: light)" srcset="./assets/neofetch-light.svg?v=2" />
    <img
      src="./assets/neofetch-light.svg?v=2"
      alt="neofetch-style card with an ASCII portrait. tiziano@bstz — OS: JVM, Kubernetes, Docker. Host: Senior Software Engineer. Kernel: Java, Quarkus, Spring Boot. Languages: Java, Quarkus, Spring, Kafka, PostgreSQL. Platform: Kubernetes, Docker. Focus: clean code, dev ergonomics, AI-assisted development. Location: Italy. Contact: Email, LinkedIn, dev.to, Stack Overflow, Writing at bstz.it. Plus a GitHub Stats section (repos, stars, commits, contributed to, followers)."
      width="880"
    />
  </picture>
</p>

### `$ cat about.md`

<!-- EDIT:ABOUT — ≤3 sentences, plain language, approachable for non-technical readers. -->
I'm a software engineer from Italy who spends most days on the JVM — Java, Quarkus, Spring Boot, shipped on Kubernetes. I care about clean code, developer ergonomics, and tooling that makes teams faster. Lately I'm also writing about how AI changes the craft of building software.
<!-- END:ABOUT -->

### `$ ls ~/.local/bin`

<!-- EDIT:TECH-BADGES — 3–9 shields.io badges, style=for-the-badge. Each: logo slug + alt = tech name. -->
<p>
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/Quarkus-4695EB?style=for-the-badge&logo=quarkus&logoColor=white" alt="Quarkus" />
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white" alt="Spring Boot" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white" alt="Kafka" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
</p>
<!-- END:TECH-BADGES -->

### `$ ls ~/selected-work`

<!-- EDIT:FEATURED-PROJECTS — 2–6 entries, most-worth-seeing first. [`name`](url) — one-line description (≤120 chars). -->
- [`jsf-autoreload`](https://github.com/basteez/jsf-autoreload) — Maven plugin that gives JSF projects a true hot-reload loop so iteration isn't minutes long.
- [`java-skills`](https://github.com/basteez/java-skills) — Curated Claude Code skills for JVM work, turning the agent into a useful Java teammate.
<!-- END:FEATURED-PROJECTS -->

### `$ tail -f writing.log`

<!-- EDIT:WRITING-LIST — Hand-curated. Series items on one bullet with arrow-chain links; standalone items as [title](url) + optional description. -->
- **BMAD**, a development approach I've been writing about: [Don't be mad, BMAD instead](https://bstz.it/p/dont-be-mad-bmad-instead/) → [Meet the crew](https://bstz.it/p/bmad-meet-the-crew/) → [BMAD in action: building TODOdoro](https://bstz.it/p/bmad-in-action-building-tododoro/)
- [AI and the Craft: are we extending ourselves, or outsourcing ourselves?](https://bstz.it/p/ai-and-the-craft-are-we-extending-ourselves-or-outsourcing-ourselves/) — on what AI-assisted development changes about the work itself
<!-- END:WRITING-LIST -->

### `$ neofetch --stats`

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=basteez&hide_border=true&area=true&custom_title=Contributions%20over%20time&theme=tokyo-night" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=basteez&hide_border=true&area=true&custom_title=Contributions%20over%20time&theme=github-light" />
    <img
      src="https://github-readme-activity-graph.vercel.app/graph?username=basteez&hide_border=true&area=true&custom_title=Contributions%20over%20time&theme=github-light"
      alt="Contributions over the last year"
    />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=basteez&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&theme=tokyonight" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=basteez&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&theme=default" />
    <img
      src="https://github-readme-stats.vercel.app/api?username=basteez&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&theme=default"
      alt="GitHub stats: stars, commits, pull requests, issues, contributed to"
      height="170"
    />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=basteez&hide_border=true&theme=tokyonight" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=basteez&hide_border=true&theme=default" />
    <img
      src="https://github-readme-streak-stats.herokuapp.com/?user=basteez&hide_border=true&theme=default"
      alt="Current contribution streak and longest streak"
      height="170"
    />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=basteez&hide_border=true&layout=compact&langs_count=8&card_width=445&exclude_repo=&theme=tokyonight" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=basteez&hide_border=true&layout=compact&langs_count=8&card_width=445&exclude_repo=&theme=default" />
    <img
      src="https://github-readme-stats.vercel.app/api/top-langs/?username=basteez&hide_border=true&layout=compact&langs_count=8&card_width=445&exclude_repo=&theme=default"
      alt="Most-used programming languages across public and private repos"
      height="170"
    />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/basteez/basteez/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/basteez/basteez/output/github-contribution-grid-snake.svg" />
    <img
      src="https://raw.githubusercontent.com/basteez/basteez/output/github-contribution-grid-snake.svg"
      alt="Animated snake eating the contribution graph"
    />
  </picture>
</p>

### `$ whois tiziano`

<!-- EDIT:CONTACT-LINKS — Single <p>. Order: LinkedIn, dev.to, Stack Overflow, Email. Each badge alt = platform name. -->
<p>
  <a href="https://linkedin.com/in/tiziano-basile-264681147"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://dev.to/basteez"><img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white" alt="dev.to" /></a>
  <a href="https://stackoverflow.com/users/1895405"><img src="https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stackoverflow&logoColor=white" alt="Stack Overflow" /></a>
  <a href="mailto:tiz.basile@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>
<!-- END:CONTACT-LINKS -->

<sub><code>tiziano@bstz:~$ exit</code></sub>
