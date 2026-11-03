from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Midterm Project</h1>
    <p>Welcome to my Flask application!</p>
    <p>CI/CD Pipeline with GitHub Actions</p>
    <p>Status: Running</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-midterm",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
