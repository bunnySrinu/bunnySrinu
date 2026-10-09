#!/usr/bin/env python3
import os
import requests
from collections import Counter
from datetime import datetime

GITHUB_USERNAME = "bunnySrinu"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

LANGUAGE_BADGES = {
    "Java": ("Java", "ED8B00", "openjdk"),
    "Python": ("Python", "3776AB", "python"),
    "JavaScript": ("JavaScript", "F7DF1E", "javascript"),
    "TypeScript": ("TypeScript", "3178C6", "typescript"),
    "Dockerfile": ("Docker", "2496ED", "docker"),
    "Shell": ("Shell", "4EAA25", "gnubash"),
    "YAML": ("YAML", "CB171E", "yaml"),
    "HTML": ("HTML", "E34F26", "html5"),
    "CSS": ("CSS", "1572B6", "css3"),
    "Bash": ("Bash", "4EAA25", "gnubash"),
    "C#": ("CSharp", "239120", "csharp"),
    "Go": ("Go", "00ADD8", "go"),
    "Kotlin": ("Kotlin", "7F52FF", "kotlin"),
    "Rust": ("Rust", "000000", "rust"),
    "PHP": ("PHP", "777BB4", "php"),
    "Ruby": ("Ruby", "CC342D", "ruby"),
    "Groovy": ("Groovy", "4298B8", "apachegroovy"),
    "PowerShell": ("PowerShell", "5391FE", "powershell"),
}

def get_headers():
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers

def fetch_json(url, params=None):
    try:
        resp = requests.get(url, headers=get_headers(), params=params)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_user_profile():
    return fetch_json(f"https://api.github.com/users/{GITHUB_USERNAME}") or {}

def get_user_repos():
    return fetch_json(
        f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
        params={"sort": "updated", "per_page": 100, "type": "owner"}
    ) or []

def build_tech_stack_html(languages):
    html = "<p align=\"left\">\n"
    if not languages:
        languages = ["Java", "Python", "Docker", "Linux", "Git"]

    for lang in languages[:8]:
        badge = LANGUAGE_BADGES.get(lang, (lang, "2E4053", "github"))
        name, color, logo = badge
        html += f'  <img src="https://img.shields.io/badge/{name}-{color}?style=for-the-badge&logo={logo}&logoColor=white" />\n'

    html += "</p>"
    return html

def build_featured_projects_html(repos):
    html = "<p align=\"left\">\n"

    featured = []
    for repo in repos:
        if repo.get("fork") or repo.get("archived"):
            continue
        if repo.get("name") in {"bunnySrinu", "bunnySrinu.github.io"}:
            continue
        featured.append(repo)

    featured = sorted(featured, key=lambda r: (r.get("stargazers_count", 0), r.get("updated_at", "")), reverse=True)[:3]

    for repo in featured:
        name = repo["name"]
        html += f'  <a href="https://github.com/{GITHUB_USERNAME}/{name}">\n'
        html += f'    <img src="https://github-readme-stats.vercel.app/api/pin/?username={GITHUB_USERNAME}&repo={name}&theme=tokyonight" />\n'
        html += "  </a>\n"

    if not featured:
        html += '  <a href="https://github.com/bunnySrinu">\n'
        html += '    <img src="https://github-readme-stats.vercel.app/api/pin/?username=bunnySrinu&repo=bunnySrinu&theme=tokyonight" />\n'
        html += "  </a>\n"

    html += "</p>"
    return html

def build_about_me(profile, repos):
    bio = profile.get("bio") or "QA / Test Automation Engineer · DevOps Enthusiast"
    top_repo = ""
    if repos:
        for repo in repos:
            if not repo.get("fork") and not repo.get("archived"):
                top_repo = repo["name"]
                break

    if top_repo:
        return f"""- 🔭 I'm currently building **automation and DevOps projects** around **{top_repo}**
- ⚙️ Interested in **CI/CD pipelines, test automation, infrastructure, and build automation**
- 🌱 Always leveling up my skills in **Selenium, Java, Maven, Docker, and GitHub Actions**
- 💬 Ask me about **test automation, QA engineering, and deployment workflows**
- 🧑‍💻 GitHub bio: **{bio}**
- 📫 Reach me on [GitHub](https://github.com/{GITHUB_USERNAME})"""
    else:
        return f"""- 🔭 I'm currently building **automation and DevOps projects**
- ⚙️ Interested in **CI/CD pipelines, test automation, infrastructure, and build automation**
- 🌱 Always leveling up my skills in **Selenium, Java, Maven, Docker, and GitHub Actions**
- 💬 Ask me about **test automation, QA engineering, and deployment workflows**
- 🧑‍💻 GitHub bio: **{bio}**
- 📫 Reach me on [GitHub](https://github.com/{GITHUB_USERNAME})"""

def get_top_languages(repos):
    counter = Counter()
    for repo in repos:
        name = repo.get("language")
        if name:
            counter[name] += 1
    return [lang for lang, _ in counter.most_common(8)]

def build_readme():
    profile = get_user_profile()
    repos = get_user_repos()
    top_languages = get_top_languages(repos)
    about_me = build_about_me(profile, repos)

    readme = f'''<h1 align="center">Hi, I'm Srinivas 👋</h1>
<h3 align="center">QA / Test Automation Engineer · DevOps Enthusiast</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=2EC4B6&center=true&vCenter=true&width=500&lines=Automating+the+boring+stuff...;Selenium+%2B+Java+%2B+TestNG;CI%2FCD+Pipeline+Expert;Docker+%26+Kubernetes;Infrastructure+as+Code" />
</p>

---

### 🧭 About Me

{about_me}

---

### 🛠️ Tech Stack

{build_tech_stack_html(top_languages)}

---

### 📌 Featured Projects

{build_featured_projects_html(repos)}

---

### 📊 GitHub Stats

<p align="left">
  <img src="https://github-readme-stats.vercel.app/api?username={GITHUB_USERNAME}&show_icons=true&theme=tokyonight&hide_border=true" height="165"/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={GITHUB_USERNAME}&theme=tokyonight&hide_border=true" height="165"/>
</p>

<p align="left">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB_USERNAME}&layout=compact&theme=tokyonight&hide_border=true" />
</p>

---

<p align="center"><i>⭐ Thanks for stopping by — feel free to explore my repos!</i></p>

<!-- AUTO-GENERATED README: Last updated {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC -->
'''

    return readme

def main():
    readme_content = build_readme()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("README generated successfully")

if __name__ == "__main__":
    main()
