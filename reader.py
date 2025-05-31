# Fortmat for questions is {CATEGORY}: {Question}

import os
import random
from termcolor import colored
from readchar import readchar

file = open("./questions.txt", encoding="utf-8")
lines = file.readlines()
file.close()

random.shuffle(lines)

completedLines = []
while True:
    os.system("cls")
    line = lines.pop()
    completedLines.append(line)
    array = [a.strip() for a in line.split(":")]
    if len(array) >= 2:
        print(colored(f"Remaining: {len(lines)}", "blue"))
        print(colored(array[0] + (" (HINT)" if len(array) >= 3 else ""), "green"), end="\n\n")
        print(array[1])
    else:
        print(colored(f"Remaining: {len(lines)}\n\n", "red"))
        print(array[0])

    key = readchar()
    if key == "s" and len(array) >= 3:
        print(array[2])
        key = readchar()
    if key == "q":    
        os.system("cls")
        exit(0)
    if key == "b":
        lines.extend(reversed(completedLines[-2:]))
        completedLines = completedLines[:-2]
    if(len(lines) == 0):
        lines, completedLines = (completedLines, lines)
        random.shuffle(lines)
