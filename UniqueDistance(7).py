import math

def find6():
    for a in range(31):
        print(a)
        for b in range(a + 1, 32):
            for c in range(b + 1, 33):
                for d in range(c + 1, 34):
                    for e in range(d + 1, 35):
                        for f in range(e + 1, 36):
                            acoords = getCoords(a)
                            bcoords = getCoords(b)
                            ccoords = getCoords(c)
                            dcoords = getCoords(d)
                            ecoords = getCoords(e)
                            fcoords = getCoords(f)
                            allDist = []
                            allDist.append((acoords[0] - bcoords[0])**2 + (acoords[1] - bcoords[1])**2)
                            allDist.append((acoords[0] - ccoords[0])**2 + (acoords[1] - ccoords[1])**2)
                            allDist.append((acoords[0] - dcoords[0])**2 + (acoords[1] - dcoords[1])**2)
                            allDist.append((acoords[0] - ecoords[0])**2 + (acoords[1] - ecoords[1])**2)
                            allDist.append((acoords[0] - fcoords[0])**2 + (acoords[1] - fcoords[1])**2)
                            allDist.append((bcoords[0] - ccoords[0])**2 + (bcoords[1] - ccoords[1])**2)
                            allDist.append((bcoords[0] - dcoords[0])**2 + (bcoords[1] - dcoords[1])**2)
                            allDist.append((bcoords[0] - ecoords[0])**2 + (bcoords[1] - ecoords[1])**2)
                            allDist.append((bcoords[0] - fcoords[0])**2 + (bcoords[1] - fcoords[1])**2)
                            allDist.append((ccoords[0] - dcoords[0])**2 + (ccoords[1] - dcoords[1])**2)
                            allDist.append((ccoords[0] - ecoords[0])**2 + (ccoords[1] - ecoords[1])**2)
                            allDist.append((ccoords[0] - fcoords[0])**2 + (ccoords[1] - fcoords[1])**2)
                            allDist.append((dcoords[0] - ecoords[0])**2 + (dcoords[1] - ecoords[1])**2)
                            allDist.append((dcoords[0] - fcoords[0])**2 + (dcoords[1] - fcoords[1])**2)
                            allDist.append((ecoords[0] - fcoords[0])**2 + (ecoords[1] - fcoords[1])**2)
                            if (len(allDist) == len(set(allDist))):
                                return acoords, bcoords, ccoords, dcoords, ecoords, fcoords

def getCoords(num):
    return math.floor(num / 6), num % 6

print(find6())