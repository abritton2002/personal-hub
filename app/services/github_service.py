from github import Github
from flask import current_app

def get_github_projects():
    token = current_app.config.get('GITHUB_TOKEN')
    username = current_app.config.get('GITHUB_USERNAME')
    if not token or not username:
        return []
    g = Github(token)
    user = g.get_user(username)
    repos = user.get_repos()
    projects = []
    for repo in repos[:5]:  # Limit to 5 most recent
        projects.append({
            'name': repo.name,
            'description': repo.description if repo.description else 'No description provided.',
            'url': repo.html_url,
            'owner': repo.owner.login
        })
    return projects

def get_repo_readme(repo_name):
    token = current_app.config.get('GITHUB_TOKEN')
    username = current_app.config.get('GITHUB_USERNAME')
    if not token or not username:
        return None
    g = Github(token)
    user = g.get_user(username)
    try:
        repo = user.get_repo(repo_name)
        readme = repo.get_readme()
        return readme.decoded_content.decode('utf-8')
    except Exception as e:
        return None 