# flipper_config.py
flipper_ip = "ADRESSE_IP"

def get_flipper_ip():
    return flipper_ip

def set_flipper_ip(ip):
    global flipper_ip
    flipper_ip = ip
