from flask import Flask


def create_app():
    # instantiate the app
    app = Flask(__name__)

    # register blueprints
    from main.ingest import ingest_blueprint
    from main.status import status_blueprint

    app.register_blueprint(ingest_blueprint)
    app.register_blueprint(status_blueprint)

    return app
