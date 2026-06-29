from flask import Flask
from config import Config
from database import db
from routes.employee_routes import employee_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(employee_bp)

@app.route("/")
def home():
    return "Employee API Running"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(debug=True)

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response