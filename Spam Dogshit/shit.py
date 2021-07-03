from requests import get
from time import sleep as wait
shit = [get("https://pastebin.com/raw/KiNUge03").text, get("https://pastebin.com/raw/KmrhMTqT").text]
i = 0
while True:
    wait(1)
    print(shit[i%2])
    i += 1
