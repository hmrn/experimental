from flask import Flask
from experimental.api.v1.health import health_blueprint
from experimental.api.v1.demo import demo_blueprint


app = Flask(__name__)
app.register_blueprint(health_blueprint)
app.register_blueprint(demo_blueprint)

if __name__ == '__main__':
    app.run()
