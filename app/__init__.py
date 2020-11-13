from flask import Flask

def create_app():
    # instantiate new object
    app = Flask(__name__)

    from app.blueprints.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    with app.app_context():
        pass

    return app