
from flask import Flask, request
import csv

app = Flask(__name__)
WA_LOG_FILE = "wa_users.csv"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    phone_number = data.get("contact", {}).get("uid")
    message_text = data.get("message", {}).get("text", "")

    if phone_number:
        with open(WA_LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([phone_number, message_text])
    return "ok", 200

if __name__ == "__main__":
    app.run(port=5001)
