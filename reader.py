import os
import random
from termcolor import colored

file = open("./questions.txt", encoding="utf-8")
lines = file.readlines()
file.close()

completedLines = []
while True:
    os.system("cls")
    line = random.choice(lines)
    completedLines.append(line)
    lines.remove(line)
    array = line.split(": ")
    if len(array) == 2:
        print(colored(f"Remaining: {len(lines)}", "blue"))
        print(colored(array[0], "green"), end="\n\n")
        print(array[1])
    else:
        print(colored(f"Remaining: {len(lines)}\n\n", "red"))
        print(array[0])
    input("")
    if(len(lines) == 0):
        lines, completedLines = (completedLines, lines)
