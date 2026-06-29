from flask import Flask, request, jsonify

app = Flask(__name__)

# Health check
@app.route("/", methods=["GET"])
def home():
    return "Backend is running successfully on AWS ECS!"

# Process API
@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    return jsonify({
        "message": f"User {name} with email {email} registered successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)