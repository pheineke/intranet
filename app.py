import base64
import os
from flask import Flask, redirect, url_for, request, render_template, session, flash
from functools import wraps
from Database import Database

class Main:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.secret_key = self.generate_secret_key()
        self.app.config.update(
            TEMPLATES_AUTO_RELOAD=True
        )

        self._configure_routes()
        self.db = Database()

    def generate_secret_key(self):
        random_bytes = os.urandom(24)
        secret_key = base64.b64encode(random_bytes).decode('utf-8')
        return secret_key

    def _configure_routes(self):
        @self.app.route('/')
        def index():
            return redirect(url_for('login'))

        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                username = request.form.get('username')
                password = request.form.get('password')
                if self.db.authenticate_user(username, password):
                    session['username'] = username
                    return redirect(url_for('home'))
                else:
                    flash('Invalid credentials. Please try again.')
            return render_template('login.html')

        @self.app.route('/register', methods=['GET', 'POST'])
        def register():
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                if self.db.register_user(username, password):
                    flash('Registration successful. You can now log in.')
                    return redirect(url_for('login'))
                else:
                    flash('Username already exists. Please choose a different one.')
            return render_template('register.html')

        @self.app.route('/home')
        @Main.login_required
        def home():
            return render_template('home.html')

        @self.app.route('/finance')
        @Main.login_required
        def finance():
            return render_template('finance.html')

        @self.app.route('/logout')
        def logout():
            session.pop('username', None)
            return redirect(url_for('login'))

    @staticmethod
    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function

    def run(self, debug=True):
        self.app.run(port=5000, debug=debug)

if __name__ == '__main__':
    main = Main()
    main.run()
