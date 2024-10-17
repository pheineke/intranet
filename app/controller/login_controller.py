from flask import redirect, url_for, request, render_template, session, flash, blueprints


bp = blueprints.Blueprint('login', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('home.index'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')