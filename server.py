from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.ai import ask_ai
from config.settings import GREETING, VERSION

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "status": "online",
        "name": "Jarvis X",
        "version": VERSION
    }

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


if __name__ == "__main__":
    print(GREETING)
    app.run(host="0.0.0.0", port=5000, debug=True)

