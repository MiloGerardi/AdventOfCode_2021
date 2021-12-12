import main

print("----------Day 4----------")

# Partie 1

print("Partie 1")

inputs = main.readFileLine(main.defPath+'day_4.txt', 'r')
if inputs[len(inputs)-1]=='':
    del inputs[len(inputs)-1]

initialNums = inputs[0].split(',')
# boards[a][b][c], a = numero de grille, b = numero de la ligne, c = numero de la colone
boards = [[inputs[i+j].split(' ') for i in range(0,5)] for j in range(2, len(inputs), 6)]
for i in range(len(boards)-1):
    for j in range(5):
        for k in range(5):
            if boards[i][j][k]=='':
                del boards[i][j][k]

def winVerif(numbers, board):
    bImage = [[0 for i in range(len(board))] for j in range(len(board))]
    for n in range(len(numbers)):
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == numbers[n]:
                    bImage[r][c] = 1
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
    nums.append(initialNums[n])
    for b in range(len(boards)):
        if winVerif(nums, boards[b]):
            winner = b
            num = n
            break
    if winner != 9999999:
        break
print('Winnig board :', winner, 'after', num+1, 'drawn numbers')
for n in range(len(nums)):
    for r in range(5):
        for c in range(5):
            if boards[winner][r][c] == nums[n]:
                boards[winner][r][c] = '0'

sum = 0
for r in range(5):
    for c in range(5):
        sum += int(boards[winner][r][c])

print('Board sum :', sum)
print('Last number drawn :', nums[-1])
print('Puzzle answer :', sum*(int(nums[-1])))
print('')



# Partie 2

print("Partie 2")
