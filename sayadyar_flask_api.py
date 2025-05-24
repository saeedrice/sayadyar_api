
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "خطا در پاسخ‌دهی: " + str(e)})

@app.route("/")
def home():
    return "Sayadyar Chatbot API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
