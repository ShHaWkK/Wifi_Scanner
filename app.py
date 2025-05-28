from flask import Flask, render_template
from scan_wifi import scan_wifi_networks, detect_evil_twin
from deauth_control import trigger_deauth

app = Flask(__name__)

@app.route("/")
def index():
    networks = scan_wifi_networks()
    evil_twins = detect_evil_twin(networks)
    return render_template("report.html", networks=networks, evil_twins=evil_twins)

@app.route("/deauth/<ap>/<client>")
def deauth(ap, client):
    result = trigger_deauth(client, ap)
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
