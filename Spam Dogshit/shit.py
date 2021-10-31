from requests import get
from time import sleep as wait
shit = [get("https://pastebin.com/raw/KiNUge03").text, get("https://pastebin.com/raw/KmrhMTqT").text]
while True:
    print(shit[0])
    print(shit[1])
