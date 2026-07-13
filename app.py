from flask import Flask

from config import Config

from models import db

from routes.dashboard import dashboard_bp
from routes.api import api_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

@app.route("/test-db")
def test_db():
    from models.crime import Crime
    return f"Total Crimes: {Crime.query.count()}"

app.register_blueprint(dashboard_bp)
app.register_blueprint(api_bp)

# Create tables when the app starts
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)