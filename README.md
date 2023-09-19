
# Story
In the age of open-source software and collaborative development, keeping track of updates to GitHub repositories has become more crucial than ever. Whether you're a developer, a project manager, or just an enthusiast, you'll find it beneficial to receive real-time updates about your favorite GitHub repositories. That's where the EVB-Pico-W5100 comes in. This project aims to combine the power of Raspberry Pi Pico, a PC server, and Telegram to create a real-time GitHub repository monitoring system.

## project purpose
The primary goal of this project is to provide real-time alerts for GitHub repository updates. By leveraging the capabilities of the Raspberry Pi Pico and Telegram's instant messaging service, users can receive immediate notifications whenever a monitored GitHub repository is updated.

## Expected Benefits
- Real-time GitHub repository monitoring
- Instant Telegram notifications
- Low-cost solution using Raspberry Pi Pico
- Easy to set up and maintain
- Scalable for monitoring multiple repositories

## Requirements
- Raspberry Pi Pico
- Micro USB cable
- Computer with internet access
- Github API Tokens
- Telegram bot

## Raspberry Pi Pico Setting
Connect the evb-pico-w5100s to the Ethernet and prepare to communicate with the PC.  
[Tutorial Guide](https://github.com/Wiznet/RP2040-HAT-MicroPython)  
For the firmware and Ethernet communication code related to the RP2040, I referenced the above GitHub to write the code  

**Basic Examples**
```python
#pico test code
from usocket import socket
from machine import Pin,SPI
import network
import time

#W5x00 chip init
def w5x00_init():
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
    nic.active(True)
    
    #None DHCP
    nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
    
    #DHCP
    #nic.ifconfig('dhcp')
    
    print('IP address :', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    
def server_loop(): 
    s = socket()
    s.bind(('192.168.1.20', 5000)) #Source IP Address
    s.listen(5)
    
    print("TEST server")
    conn, addr = s.accept()
    print("Connect to:", conn, "address:", addr) 
    print("Loopback server Open!")
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL':
            conn.send(data)
            
  def main():
    w5x00_init()
    
###TCP SERVER###
    #server_loop()

###TCP CLIENT###
    client_loop()

if __name__ == "__main__":
    main()
```

## PC Server Setting
```python

```
```python
#Code to send from PC server to Pico
import socket

IP_ADDRESS = 'Your Server IP'
PORT = 5000  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP_ADDRESS, PORT))

client_socket.sendall("Hello Pico".encode())

data = client_socket.recv(1024)
print('Received:', data.decode())
```

**steps**
- Install Dependencies: Install the required Python packages using pip.
- Run Server Code: Execute the provided Python script to start the server.
- Test Connection: Make sure the server can communicate with the Raspberry Pi Pico and fetch data from GitHub.


## Telegram

[Reference](https://maker.wiznet.io/simons/projects/please-fridge-with-raspberrypi-pico/)
```python
# Telegram Bot Token
TELEGRAM_TOKEN = "Your Token"
CHAT_ID = "Your ID"

# Send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    urequests.post(url, json=data)

```

**steps**
- Create a Bot: Use the Telegram BotFather to create a new bot.
- Get Token: Obtain the API token for your bot.
- Configure Code: Update the Raspberry Pi Pico code with your Telegram bot's API token.
- Test Notifications: Ensure that you can receive Telegram notifications from the Raspberry Pi Pico.

## Communication
The Raspberry Pi Pico and the PC server communicate over a local network. The server fetches the latest updates from GitHub and sends this information to the Raspberry Pi Pico. The Pico then forwards these updates to Telegram.


## Result
<img width="222" alt="스크린샷 2023-09-19 오후 5 06 35" src="https://github.com/wiznetmaker/GitHub_Repository_Monitoring/assets/112835087/b02cfe06-27bc-4993-a4b3-5940199f6d33">


Upon successful setup, you'll start receiving real-time Telegram notifications whenever there's an update to the monitored GitHub repository. This project offers a cost-effective and straightforward way to stay updated on your favorite GitHub projects.  

Feel free to expand upon this project by adding more features, such as monitoring multiple repositories or integrating with other messaging platforms.


**Discover open source repository treasures together with Pico**
## For more code
[maker site](https://maker.wiznet.io/simons/projects/real-time-github-repository-monitoring-with-raspberry-pi-pico-and-telegram/?serob=rd&serterm=month)
