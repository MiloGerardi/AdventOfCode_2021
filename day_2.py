import main

print("----------Day 2----------")

# Partie 1

inputs = main.splitText(main.readFile(main.defPath + "day_2.txt", 'r'), " ")
forward = 0
depth = 0
for i in range(0, len(inputs)):
    if inputs[i] == 'forward':
        forward += int(inputs[i + 1])
    if inputs[i] == 'up':
        depth -= int(inputs[i + 1])
    if inputs[i] == 'down':
        depth += int(inputs[i + 1])

print("Partie 1")
print("resultat =",forward*depth)


print("")

# Partie 2

inputs = main.splitText(main.readFile(main.defPath + "day_2.txt", 'r'), " ")
forward = 0
depth = 0
aim = 0
for i in range(0, len(inputs)):
    if inputs[i] == 'forward':
        forward += int(inputs[i + 1])
        depth += aim * int(inputs[i + 1])
    if inputs[i] == 'up':
        aim -= int(inputs[i + 1])
    if inputs[i] == 'down':
        aim += int(inputs[i + 1])

print("Partie 2")
print("resultat =",forward*depth)
print("-------------------------")
