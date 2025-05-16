from flask import Blueprint, render_template, request
from app.services.github_service import get_repo_readme

bp = Blueprint('github', __name__, url_prefix='/projects')

# Placeholder for future GitHub project routes 

@bp.route('/<repo_name>/readme')
def repo_readme(repo_name):
    readme_content = get_repo_readme(repo_name)
    if readme_content is None:
        readme_content = 'README not found or could not be loaded.'
    return render_template('repo_readme.html', repo_name=repo_name, readme_content=readme_content) 