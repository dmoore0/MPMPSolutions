capacity = int(input("Please input the train's fuel capacity. "))
distance = int(input("Please input the total distance to be traveled. "))

elapsed = 0
iteration = 0

while (elapsed < distance):
    prevelapsed = elapsed
    elapsed += capacity / (2 * iteration + 1)
    iteration += 1

print ("The total fuel needed is " + str((iteration - 1) * capacity + (distance - prevelapsed) * ((iteration - 1) * 2 + 1)) + " units.")