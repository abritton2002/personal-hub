from flask import Blueprint, render_template
from app.services.github_service import get_github_projects
from app.services.substack_service import get_latest_posts

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    github_projects = get_github_projects()
    substack_posts = get_latest_posts()
    return render_template('index.html', 
                         projects=github_projects,
                         posts=substack_posts) 