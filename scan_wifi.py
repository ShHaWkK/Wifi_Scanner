import subprocess
import re

def scan_wifi_networks():
    result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], encoding="utf-8")
    networks = []
    lines = result.splitlines()
    ssid = None
    security = None
    bssid = None
    signal = None
    channel = None

    for line in lines:
        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":", 1)[1].strip()
        elif "Authentication" in line:
            security = line.split(":", 1)[1].strip()
        elif "BSSID" in line:
            bssid = line.split(":", 1)[1].strip()
        elif "Signal" in line:
            signal = line.split(":", 1)[1].strip()
        elif "Channel" in line:
            channel = line.split(":", 1)[1].strip()
            if ssid and bssid:
                networks.append({
                    "ssid": ssid,
                    "bssid": bssid,
                    "security": security,
                    "signal": signal,
                    "channel": channel
                })

    return networks

def detect_evil_twin(networks):
    ssid_map = {}
    suspects = []

    for net in networks:
        ssid = net['ssid']
        if ssid not in ssid_map:
            ssid_map[ssid] = []
        ssid_map[ssid].append(net)

    for ssid, nets in ssid_map.items():
        if len(nets) > 1:
            suspects.append({
                "ssid": ssid,
                "entries": nets
            })

    return suspects
