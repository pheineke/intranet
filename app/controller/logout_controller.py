from flask import redirect, url_for, request, render_template, session, flash, blueprints

bp = blueprints.Blueprint('logout', __name__)

@bp.route('/')
def index():
    return redirect(url_for('login.index'))