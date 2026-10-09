#!/usr/bin/env python3
"""
Auto-generate README.md from GitHub repositories.
This script fetches your repos and dynamically creates a README with featured projects.
"""

import requests
import os
from datetime import datetime

# Configuration
GITHUB_USERNAME = "bunnySrinu"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

# Featured project repos (manually curated)
FEATURED_REPOS = [
    "SeleniumAutomationPOM",
    "DevOps"
]

# Tech stack badges
TECH_STACK = [
    ("Java", "ED8B00", "openjdk"),
    ("Selenium", "43B02A", "selenium"),
    ("TestNG", "EF2D5E", "testinglibrary"),
    ("Maven", "C71A36", "apachemaven"),
    ("Git", "F05032", "git"),
    ("Jenkins", "D24939", "jenkins"),
    ("Docker", "2496ED", "docker"),
    ("Linux", "FCC624", "linux"),
]

def get_github_repos():
    """Fetch all repos for the user."""
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    params = {
        "sort": "stars",
        "per_page": 100,
        "type": "owner"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repos: {e}")
        return []

def get_repo_details(repo_name):
    """Fetch specific repo details."""
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repo {repo_name}: {e}")
        return {}

def build_tech_stack_html():
    """Build HTML for tech stack badges."""
    html = "<p align=\"left\">\n"
    for tech_name, color, logo in TECH_STACK:
        html += f'  <img src="https://img.shields.io/badge/{tech_name}-{color}?style=for-the-badge&logo={logo}&logoColor=white" />\n'
    html += "</p>"
    return html

def build_featured_projects_html():
    """Build HTML for featured projects with dynamic data."""
    html = "<p align=\"left\">\n"
    
    for repo_name in FEATURED_REPOS:
        repo = get_repo_details(repo_name)
        if repo:
            html += f'  <a href="https://github.com/{GITHUB_USERNAME}/{repo_name}">\n'
            html += f'    <img src="https://github-readme-stats.vercel.app/api/pin/?username={GITHUB_USERNAME}&repo={repo_name}&theme=tokyonight" />\n'
            html += f'  </a>\n'
    
    html += "</p>"
    return html

def build_readme():
    """Generate the complete README content."""
    
    readme = f"""<h1 align="center">Hi, I'm Srinivas 👋</h1>
<h3 align="center">QA / Test Automation Engineer · DevOps Enthusiast</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=2EC4B6&center=true&vCenter=true&width=500&lines=Automating+the+boring+stuff...;Selenium+%2B+Java+%2B+TestNG;CI%2FCD+Pipeline+Expert;Docker+%26+Kubernetes;Infrastructure+as+Code" />
</p>

---

### 🧭 About Me

- 🔭 I'm currently building **test automation frameworks** using the Page Object Model pattern
- ⚙️ Interested in **DevOps practices** — CI/CD pipelines, build automation, and infrastructure
- 🌱 Always leveling up my skills in test automation and deployment workflows
- 💬 Ask me about Selenium, TestNG, Maven, or Java-based test frameworks
- 📫 Reach me on [GitHub](https://github.com/{GITHUB_USERNAME})

---

### 🛠️ Tech Stack

{build_tech_stack_html()}

---

### 📌 Featured Projects

{build_featured_projects_html()}

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

<!-- AUTO-GENERATED README: Last updated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC -->
"""
    
    return readme

def save_readme(content):
    """Save README.md to the repo root."""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ README.md generated successfully!")

def main():
    """Main execution."""
    print(f"🔄 Generating README for {GITHUB_USERNAME}...")
    
    # Generate and save README
    readme_content = build_readme()
    save_readme(readme_content)
    
    print("✅ README update complete!")

if __name__ == "__main__":
    main()
