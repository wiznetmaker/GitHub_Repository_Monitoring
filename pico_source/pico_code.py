from usocket import socket
from machine import Pin, SPI
import network
import time
import urequests  # MicroPython requests library

# Telegram Bot Token
TELEGRAM_TOKEN = "Your Tokens"
CHAT_ID = "Your ID"

# Send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    urequests.post(url, json=data)

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    
    #None DHCP
    nic.ifconfig(('Your IP','255.255.255.0','Your IP Gateway','8.8.8.8'))
    
    #DHCP
    #nic.ifconfig('dhcp')
    
    print('IP address :', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    
def server_loop():
    s = socket()
    s.bind(('Your IP', 5000))
    s.listen(5)
    
    print("TEST server")
    conn, addr = s.accept()
    print("Connect to:", conn, "address:", addr)
    print("Loopback server Open!")
    
    while True:
        data = conn.recv(2048)
        repo_info = data.decode('utf-8')
        print(repo_info)
        
        if repo_info != 'NULL':
            conn.send(data)
            send_telegram_message(f"New update found in repo: {repo_info}")

def main():
    w5x00_init()
    server_loop()

if __name__ == "__main__":
    main()
