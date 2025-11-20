import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("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"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

