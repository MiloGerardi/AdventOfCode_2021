import main

print("----------Day 5----------")

# Partie 1

print("Partie 1")
inputs = main.readFileLine(main.defPath + 'day_5.txt', 'r')
# Split la liste de la manière suivante :
# inputs[a][b][c] avec a = ligne    b = point(1 ou 2)   c = valeur(x ou y)
inputs = [inputs[i].split(' -> ') for i in range(len(inputs)-1)]
inputs = [[inputs[i][j].split(',') for j in range(2)] for i in range(len(inputs)-1)]
#Transforme le string en int
for i in range(len(inputs)-1):
    for j in range(len(inputs[i])-1):
        for k in range(len(inputs[i][j])-1):
            inputs[i][j][k] = int(inputs[i][j][k])
# Créer la grille (map)
grid = [[0 for i in range(1000)] for j in range(1000)]