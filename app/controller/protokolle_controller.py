from flask import redirect, url_for, request, render_template, session, flash, blueprints

bp = blueprints.Blueprint('protokolle', __name__)

@bp.route('/')
def index():
    return render_template('protokolle.html')

@bp.route('/create')
def create():
    return render_template('protokolle_create.html')