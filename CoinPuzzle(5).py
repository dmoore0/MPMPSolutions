import math
import copy

def createPuzzle(n):
    puzzle = list()
    for i in range(1, n + 1):
        row = list()
        for j in range(i):
            row.append("coin")
        puzzle.append(row)
    return puzzle

def getUniqueStarts(puzzle):
    uniqueStarts = list()
    dup = copy.deepcopy(puzzle)
    for i in range(len(dup)):
        for j in range(len(dup[i])):
            dup[i][j] = "empty"
            add = True
            for start in uniqueStarts:
                if (dup == rotateCW(start) or dup == rotateCW(rotateCW(start)) or dup == flipHor(start) or dup == flipHor(rotateCW(start)) or dup == flipHor(rotateCW(rotateCW(start)))):
                    add = False
            if (add == True):
                uniqueStarts.append(copy.deepcopy(dup))
            dup[i][j] = "coin"
    return uniqueStarts

def rotateCW(puzzle):
    rotated = list()
    for i in range(len(puzzle) - 1, -1, -1):
        row = list()
        for j in range(len(puzzle) - 1, i - 1, -1):
            row.append(puzzle[j][j - i])
        rotated.append(row)
    return rotated

def flipHor(puzzle):
    flipped = list()
    for i in puzzle:
        flipped.append([ele for ele in reversed(i)])
    return flipped

def genMoves(state):
    moves = list()
    for i in range(len(state)):
        for j in range(len(state[i])):
            if (state[i][j] == "empty"):
                potstart = list()
                potstart.append([i, j + 2])
                potstart.append([i, j - 2])
                potstart.append([i + 2, j])
                potstart.append([i - 2, j])
                potstart.append([i + 2, j + 2])
                potstart.append([i - 2, j - 2])
                for k in potstart:
                    if (k[0] >= 0 and k[1] >= 0 and k[1] <= k[0] and k[0] < len(state)):
                        potmid = [int((k[0] + i) / 2), int((k[1] + j) / 2)]
                        if (state[k[0]][k[1]] != "empty" and state[potmid[0]][potmid[1]] != "empty"):
                            newmove = list()
                            newmove.append(k)
                            newmove.append(potmid)
                            newmove.append([i, j])
                            moves.append(newmove)
    return moves

def checkSolved(state):
    count = 0
    for i in state:
        for j in i:
            if (j != "empty"):
                count += 1
    if (count <= 1):
        return True
    return False

def getMinMoves(n):
    puzzle = createPuzzle(n)
    startingPositions = getUniqueStarts(puzzle)
    res = list()
    for i in startingPositions:
        res.append(recursiveSolve(i, None, 0))
    minimum = float('inf')
    moveset = []
    for i in range(len(res)):
        if (res[i][0] < minimum):
            minimum = res[i][0]
            moveset = res[i][1]
            moveset.insert(0, startingPositions[i])
    print("The minimum number of moves is " + str(minimum) + ", which is " + str(n * (n + 1) // 2 - 2 - minimum) + " less than the worst case of " + str(n * (n + 1) // 2 - 2) + ".")
    print("The state set is:")
    printStates(moveset)

def recursiveSolve(state, lastCoin, currentCost):
    if (checkSolved(state)):
        return [currentCost, []]
    moves = genMoves(state)
    if (len(moves) <= 0):
        return [float('inf'), []]
    results = list()
    for i in moves:
        newState = copy.deepcopy(state)
        newState[i[0][0]][i[0][1]] = "empty"
        newState[i[1][0]][i[1][1]] = "empty"
        newState[i[2][0]][i[2][1]] = "coin"
        if (i[0] == lastCoin):
            results.append(recursiveSolve(newState, i[2], currentCost))
            results[len(results) - 1][1].insert(0, newState)
        else:
            results.append(recursiveSolve(newState, i[2], currentCost + 1))
            results[len(results) - 1][1].insert(0, newState)
    mini = float('inf')
    moves = []
    for i in range(len(results)):
        if (results[i][0] < mini):
            mini = results[i][0]
            moves = results[i][1]
    return [mini, moves]

def printStates(moveset):
    for i in moveset:
        print()
        rowlength = len(rowToString(i[len(i) - 1]))
        for j in i:
            print(rowToString(j, rowlength))

def rowToString(row, length = None):
    coin = 'O'
    empty = 'X'
    space = ' '
    string = ""
    first = True
    for i in row:
        if (first):
            first = False
        else:
            string = string + " "
        if (i == "empty"):
            string = string + empty
        else:
            string = string + coin
    spaces = ""
    if (length != None):
        for i in range(int((length - len(string)) / 2)):
            spaces = spaces + space
    return spaces + string

getMinMoves(4)