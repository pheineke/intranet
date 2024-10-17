from flask import Flask, redirect, url_for, request, render_template, session, flash




def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True
    )

    from app.controller.login_controller import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/')
    
    from app.controller.logout_controller import bp as logout_bp
    app.register_blueprint(logout_bp, url_prefix='/logout')

    from app.controller.home_controller import bp as home_bp
    app.register_blueprint(home_bp, url_prefix='/home')

    return app