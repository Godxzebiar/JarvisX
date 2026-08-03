from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from modules.ai import ask_ai
from config.settings import GREETING, VERSION

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory("www", "index.html")

     @app.route("/<path:path>")
def static_files(path):
    return send_from_directory("www", path)


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "Please send a message."}), 400

        reply = ask_ai(data["message"])

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server Error: {e}"
        }), 500


import os

if __name__ == "__main__":
    print(GREETING)
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
