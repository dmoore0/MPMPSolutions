#import math
import time

def containsDupes(series):
    for i, nums1 in enumerate(series):
        for j, nums2 in enumerate(series):
            if i != j:
                if nums1 == nums2:
                    return (i, j)
    return False

def check14(series, lowlimit, highlimit):
    for i in range(lowlimit, highlimit + 1):
        if (series[i][0] + series[i][1] + series[i][2] != 14):
            return False
    return True

def allUnique(series, lowlimit, highlimit):
    for i in range(lowlimit, highlimit + 1):
        if (series[i][0] == series[i][1] or series[i][0] == series[i][2] or series[i][1] == series[i][2]):
            return False
    return True

def checkSecondNotMultiples(series):
    if (series[1][0] % 7 != 0 or series[1][1] % 7 != 0 or series[1][2] % 7 != 0):
        return True
    return False

for i in range(-50, 51):
    for j in range(i, 51):
        for k in range(j, 51):
            # if (i + j + k == 14):
            series = list()
            series.append((i, j, k))
            while(containsDupes(series) == False):
                x = abs(series[len(series) - 1][0] - series[len(series) - 1][1])
                y = abs(series[len(series) - 1][0] - series[len(series) - 1][2])
                z = abs(series[len(series) - 1][1] - series[len(series) - 1][2])
                if (x > y):
                    if (x > z):
                        if (y > z):
                            series.append((z, y, x))
                        else:
                            series.append((y, z, x))
                    else:
                        series.append((y, x, z))
                else:
                    if (x > z):
                        series.append((z, x, y))
                    else:
                        if (y > z):
                            series.append((x, z, y))
                        else:
                            series.append((x, y, z))
            limits = containsDupes(series)
            # print(limits)
            # print(series)
            if (check14(series, limits[0], limits[1])):
                if (checkSecondNotMultiples(series)):
                    print(series)
                    if (allUnique(series, limits[0], limits[1])):
                        print("All numbers in each cycle iteration are unique")
                    lastVal = series[len(series) - 1]
                    if (lastVal[0] != 0 or lastVal [1] != 7 or lastVal[2] != 7):
                        print("Not 0, 7, 7")
                #time.sleep(1)


# series = list()
# series.append((5, 7, 8))
# print(containsDupes(series))

# series = list()
# series.append((5, 7, 8))
# series.append((5, 7, 9))
# print(containsDupes(series))
# series = list()
# x = -50
# y = -50
# z = -50
# series.append((x, y, z))
# x = 0
# y = 0
# z = 0
# series.append((x, y, z))
# x = 0
# y = 0
# z = 0
# series.append((x, y, z))
# print(containsDupes(series))