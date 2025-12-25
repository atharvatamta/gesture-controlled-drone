import socket
from communication.network_config import ESP32_IP, ESP32_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_command(command):
    try:
        sock.sendto(command.encode(), (ESP32_IP, ESP32_PORT))
    except OSError as e:
        print("⚠️ UDP send failed:", e)
        # Do NOT crash the program
        pass
