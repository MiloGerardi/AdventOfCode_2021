import main

print("----------Day 3----------")

# Partie 1

print("Partie 1")

inputs = main.splitText(main.readFile(main.defPath + "day_3.txt", 'r'), " ")
# Cration d'une liste à deux dimmensions avec tt les char de inputs, ligne par ligne
inputs2 = [[inputs[i][j] for j in range(len(inputs[0]))] for i in range(len(inputs))]
gamma = ''
epsilon = ''
# Compte le nombre d'itération de '1' puis compare avec le nombre de ligne
# En deduit le bit de gamma correspondant
for j in range(len(inputs[0])):
    iteration = 0
    for i in range(len(inputs)):
        iteration += int(inputs2[i][j])
    if iteration >= len(inputs) / 2:
        gamma += '1'
    else:
        gamma += '0'
# inversion des bits pour epsilon
for i in range(len(gamma)):
    if gamma[i] == '0':
        epsilon += '1'
    else:
        epsilon += '0'
gammaDec = int(gamma, 2)
epsilonDec = int(epsilon, 2)
print("gamma =", gamma, "=", gammaDec)
print("epsilon =", epsilon, "=", epsilonDec)
print("resultat = ", gammaDec * epsilonDec)

print("")

# partie 2

print("Partie 2")

o2rating = 0
co2rating = 0
inputs = main.splitText(main.readFile(main.defPath + "day_3.txt", 'r'), " ")
o2list = inputs
co2list = inputs
# Cration d'une liste à deux dimmensions avec tt les char de inputs, ligne par ligne
inputs2D = [[inputs[i][j] for j in range(len(inputs[0]))] for i in range(len(inputs))]
# Compte le nombre d'itération de '1' puis compare avec le nombre de ligne
# En deduit le bit de gamma correspondant


# recherche de o2
for j in range(len(inputs2D[0])):
    list = o2list
    list2D = [[list[i][j] for j in range(len(list[0]))] for i in range(len(list))]
    o2list = []
    iteration = 0
    for i in range(len(list)):
        iteration += int(list[i][j])
    if iteration >= len(list) / 2:
        val = 1
    else:
        val = 0
        iteration = len(list) - iteration

    for i in range(len(list)):
        if list[i][j] == str(val):
            o2list.append(list[i])
    if len(o2list) == 1:
        break

# Recherche de co2
for j in range(len(inputs2D[0])):
    list = co2list
    list2D = [[list[i][j] for j in range(len(list[0]))] for i in range(len(list))]
    co2list = []
    iteration = 0
    for i in range(len(list)):
        iteration += int(list[i][j])
    if iteration >= len(list) / 2:
        val = 0
    else:
        val = 1
        iteration = len(list) - iteration

    for i in range(len(list)):
        if list[i][j] == str(val):
            co2list.append(list[i])
    if len(co2list) == 1:
        break

    # print("bit minoritaire :", val, "avec", iteration, 'iterations  | ', "nombre de valeurs", len(co2list))

print("oxygen generator rating :", o2list[0], "=", int(o2list[0], 2))
print("CO2 scrubber rating :", co2list[0], "=", int(co2list[0], 2))
print("resultat =", int(o2list[0], 2) * int(co2list[0], 2))
