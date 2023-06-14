import os
import random
from termcolor import colored

file = open("C:/Users/jacob/OneDrive/Plocha/psiaQuestions.txt", encoding="utf-8")
lines = file.readlines()
file.close()

completedLines = []
while True:
    os.system("cls")
    line = random.choice(lines)
    completedLines.append(line)
    lines.remove(line)
    print(colored(f"Remaining: {len(lines)}", "blue"))
    print(colored(line.split(": ")[0], "green"), end="\n\n")
    print(colored(line.split(": ")[1]))
    input("")
    if(len(lines) == 0):
        lines, completedLines = (completedLines, lines)
