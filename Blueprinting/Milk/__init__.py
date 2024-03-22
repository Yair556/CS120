from flask import Flask

def create_app(): # config_class=Config
    app = Flask(__name__)

    # Create the database tables
    with app.app_context():

        # Import Blueprints
        from .auth.routes import auth_bp
        from .home.routes import home_bp


    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(home_bp, url_prefix='/home')

    return app