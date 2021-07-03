from random import randint

hello = open("curselist.txt", "r")
words = [line.strip("\n") for line in hello if line != "\n"]

def random_curse():
    return words[randint(0,len(words)]

def random_curses(amount=2):
    curselist = []
    for i in range(amount):
        curselist.append(words[randint(0,len(words))])
    return curselist
