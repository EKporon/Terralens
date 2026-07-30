from flask import Flask


from config import Config


from routes import (
    home_bp,
    api_bp,
    errors_bp
)



def create_app():


    app = Flask(__name__)


    app.config.from_object(
        Config
    )


    app.register_blueprint(
        home_bp
    )


    app.register_blueprint(
        api_bp
    )


    app.register_blueprint(
        errors_bp
    )



    return app





if __name__ == "__main__":


    app = create_app()



    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
