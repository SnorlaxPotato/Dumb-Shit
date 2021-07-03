from requests import get
from time import sleep as wait
dogshit = get("https://pastebin.com/raw/KmrhMTqT").text
while True:
    wait(1)
    print(dogshit)
