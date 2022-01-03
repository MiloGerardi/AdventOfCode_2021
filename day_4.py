import main

print("----------Day 4----------")

# Partie 1

print("Partie 1")

inputs = main.readFileLine(main.defPath + 'day_4.txt', 'r')
if inputs[len(inputs) - 1] == '':
    del inputs[len(inputs) - 1]

initialNums = inputs[0].split(',')
# Stock toutes les valeurs des grilles de bingo dans un tableau à trois dimmensions
# boards[a][b][c], a = numero de grille, b = numero de la ligne, c = numero de la colone
boards = [[inputs[i + j].split(' ') for i in range(0, 5)] for j in range(2, len(inputs), 6)]
boards2 = boards
# Suprime les entrées vides
for i in range(len(boards) - 1):
    for j in range(5):
        for k in range(5):
            if boards[i][j][k] == '':
                del boards[i][j][k]

# Verifie si une board est gagnante en fonction des nombres tirés
def winVerif(numbers, board):
    # Créer une board vide (que des 0)
    bImage = [[0 for i in range(len(board))] for j in range(len(board))]
    # Remplace un 0 par un 1 si le numero est tiré
    for n in range(len(numbers)):
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == numbers[n]:
                    bImage[r][c] = 1
    # additionne chaque ligne et chaque colone
    # si le resulat d'une ligne/colone = à la longeur de celle-ci, c'est gagné
    #
    # Exemple de bImage :
    # 1  1  0  1  0 = 3
    # 0  0  0  0  1 = 1
    # 0  0  1  1  0 = 2
    # 1  1  1  1  1 = 5 --> gagné
    # 0  1  0  0  0 = 1
    #
    countr = 0
    countc = 0
    for r in range(len(board)):
        for c in range(len(board)):
            countr += bImage[r][c]
            countc += bImage[c][r]
        if countr == len(board) or countc == len(board):
            return True
        else:
            countr = 0
            countc = 0

    return False


nums = []
winner = 9999999
num = 0
for n in range(len(initialNums)):
    # ajoute un numero à liste des numeros tirés
    nums.append(initialNums[n])
    # verifie chaque board
    for b in range(len(boards)):
        if winVerif(nums, boards[b]):
            winner = b
            num = n
            break
    if winner != 9999999:
        break
print('Winning board :', winner, 'after', num + 1, 'drawn numbers')
for n in range(len(nums)):
    for r in range(5):
        for c in range(5):
            if boards[winner][r][c] == nums[n]:
                boards[winner][r][c] = '0'

boardSum = 0
for r in range(5):
    for c in range(5):
        boardSum += int(boards[winner][r][c])

print('Board sum :', boardSum)
print('Last number drawn :', nums[-1])
print('Puzzle answer :', boardSum * (int(nums[-1])))
print('')

# Partie 2

print("Partie 2")

boards = boards2
nums = []
tirage=0
while len(boards)!=1:
    nums.append(initialNums[tirage])
    for i in range(len(boards)):
        try :
            if winVerif(nums, boards[i]) :
                del boards[i]
        except :
            break
    tirage+=1

for n in range(len(nums)):
    for r in range(5):
        for c in range(5):
            if boards[0][r][c] == nums[n]:
                boards[0][r][c] = '0'

boardSum = 0
for r in range(5):
    for c in range(5):
        boardSum += int(boards[0][r][c])
print(boards)
print(boardSum)
lastNum=nums[len(nums)-1]
print(nums)
print(19*325)