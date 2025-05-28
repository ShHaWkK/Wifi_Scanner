from flask import Flask, render_template, request, redirect, url_for
from scan_wifi import scan_wifi_networks, detect_evil_twin
from deauth_control import trigger_deauth, check_flipper_connection
from flipper_config import set_flipper_ip, get_flipper_ip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ip = request.form.get("flipper_ip")
        set_flipper_ip(ip)
        return redirect(url_for('scan'))

    return render_template("index.html", flipper_ip=get_flipper_ip(), status=check_flipper_connection())

@app.route("/scan")
def scan():
    networks = scan_wifi_networks()
    evil_twins = detect_evil_twin(networks)
    return render_template("report.html", networks=networks, evil_twins=evil_twins, flipper_ip=get_flipper_ip())

@app.route("/deauth/<ap>/<client>")
def deauth(ap, client):
    result = trigger_deauth(client, ap)
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
