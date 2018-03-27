from flask import Flask
from experimental.api.v1.health import health_blueprint


app = Flask(__name__)
app.register_blueprint(health_blueprint)

if __name__ == '__main__':
    app.run()
