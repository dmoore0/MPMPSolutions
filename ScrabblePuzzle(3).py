scrabbleLetters = [[9, "A", 1], # Count, Letter, Value
[2, "B", 3],
[2, "C", 3],
[4, "D", 2],
[12, "E", 1],
[2, "F", 4],
[3, "G", 2],
[2, "H", 4],
[9, "I", 1],
[1, "J", 8],
[1, "K", 5],
[4, "L", 1],
[2, "M", 3],
[6, "N", 1],
[8, "O", 1],
[2, "P", 3],
[1, "Q", 10],
[6, "R", 1],
[4, "S", 1],
[6, "T", 1],
[4, "U", 1],
[2, "V", 4],
[2, "W", 4],
[1, "X", 8],
[2, "Y", 4],
[1, "Z", 10],
[2, " ", 0]]

zeroes = []
ones = []
twos = []
threes = []
fours = []
fives = []
eights = []
tens = []
for letter in scrabbleLetters:
    value = letter[2]
    if (value == 0):
        zeroes.append(list([letter[0], letter[1]]))
    elif (value == 1):
        ones.append(list([letter[0], letter[1]]))
    elif (value == 2):
        twos.append(list([letter[0], letter[1]]))
    elif (value == 3):
        threes.append(list([letter[0], letter[1]]))
    elif (value == 4):
        fours.append(list([letter[0], letter[1]]))
    elif (value == 5):
        fives.append(list([letter[0], letter[1]]))
    elif (value == 8):
        eights.append(list([letter[0], letter[1]]))
    elif (value == 10):
        tens.append(list([letter[0], letter[1]]))

print(str(zeroes) + "     " + str(len(zeroes)))
print(str(ones) + "     " + str(len(ones)))
print(str(twos) + "     " + str(len(twos)))
print(str(threes) + "     " + str(len(threes)))
print(str(fours) + "     " + str(len(fours)))
print(str(fives) + "     " + str(len(fives)))
print(str(eights) + "     " + str(len(eights)))
print(str(tens) + "     " + str(len(tens)))

values = [0, 1, 2, 3, 4, 5, 8, 10]
max = [2, 68, 7, 8, 10, 1, 2, 2]
def get7TileScoreCombinations(score):
    count = 0
    valueList = []
    for first in range(8):
        for second in range(first, 8):
            for third in range(second, 8):
                for fourth in range(third, 8):
                    for fifth in range(fourth, 8):
                        for sixth in range(fifth, 8):
                            for seventh in range(sixth, 8):
                                possibleList = list([values[first], values[second], values[third], values[fourth], values[fifth], values[sixth], values[seventh]])
                                if (values[first] + values[second] + values[third] + values[fourth] + values[fifth] + values[sixth] + values[seventh] == score
                                    and possibleList.count(0) <= 2 and possibleList.count(5) <= 1 and possibleList.count(8) <= 2 and possibleList.count(10) <= 2):
                                    valueList.append(possibleList)
                                    print(possibleList)
    for lists in valueList:
        pass
    return count

def getAllUniqueCombinations(list):
    return

print(get7TileScoreCombinations(46))