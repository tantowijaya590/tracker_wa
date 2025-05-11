
from flask import Flask, request, redirect
import csv
from datetime import datetime
import requests

app = Flask(__name__)

LOG_FILE = "click_logs.csv"
REDIRECT_URL = "https://google.com"  # Ganti dengan link tujuan asli

def get_country(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        return res.get("countryCode", "UNKNOWN")
    except:
        return "ERROR"

@app.route("/track")
def track():
    user_ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    track_id = request.args.get("id", "UNKNOWN")
    country = get_country(user_ip)

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), track_id, user_ip, country, user_agent])
    
    return redirect(REDIRECT_URL, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
