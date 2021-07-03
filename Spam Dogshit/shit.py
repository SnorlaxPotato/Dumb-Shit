from requests import get
from time import sleep as wait
normal_dog = get("https://pastebin.com/raw/KiNUge03").text
dogshit = get("https://pastebin.com/raw/KmrhMTqT").text
while True:
    wait(1)
    print(dogshit)
