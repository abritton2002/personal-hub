from flask import Blueprint, render_template, request, redirect, url_for
from app.models.entry import Entry
from app import db

bp = Blueprint('content', __name__, url_prefix='/journal')

@bp.route('/', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        if title and body:
            entry = Entry(title=title, body=body)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('content.journal'))
    entries = Entry.query.order_by(Entry.created_at.desc()).all()
    return render_template('journal.html', entries=entries)

# Placeholder for future journal/content routes 