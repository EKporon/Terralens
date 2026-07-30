from flask import Flask

from config import Config


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)


    @app.route("/")
    def home():

        return """
        <h1>TerraLens 🌍</h1>
        <p>
        Know the Land Before You Buy It.
        </p>
        """


    return app



if __name__ == "__main__":

    app = create_app()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
