
def checkMillion(first, second):
    if (first == 0 and second == 0):
        return False
    if (first > 1000000 or second > 1000000):
        return False
    elif (first == 1000000):
        return 1
    elif (second == 1000000):
        return 2
    days = 2
    while second < 1000000:
        print(first)
        print(second)
        print()
        temp = second
        second = first + temp
        first = temp
        days += 1
    if (second > 1000000):
        return False
    return days

maxdays = 0
firstdeposit = 0
seconddeposit = 0
for i in range(153, 155):
    for j in range(143, 145):
        answer = checkMillion(i, j)
        print(answer)
        if (answer != False):
            if (answer > maxdays):
                maxdays = answer
                firstdeposit = i
                seconddeposit = j
print(maxdays)
print(firstdeposit)
print(seconddeposit)

