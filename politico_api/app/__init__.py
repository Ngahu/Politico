""" Create our application """


from flask import Flask

from instance.config import APP_CONFIG




def create_app(config_name):
    """ Registering app confingurations """
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[config_name])

    from app.api.v1.resources.admin_endpoints import (
        index,
        all_parties,
        view_two
        )

    from app.api.v1 import version_1
    app.register_blueprint(version_1)


    return app

    