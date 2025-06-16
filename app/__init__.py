from flask import Flask

from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__, template_folder='')
    app.config.from_object(DevelopmentConfig())

    from .blueprints import all_blueprints
    for blueprint, prefix in all_blueprints: #register all blueprints
        app.register_blueprint(blueprint=blueprint, url_prefix=prefix )

    return app