'''
print("Two-dimentional arrays")
a = [[10, 20, 30], [40, 50, 60]]
n = len(a)
print("Count of stirngs in array = {}\na[0] - first string: {}\na[1] - second string: {}\n".format(n, a[0], a[1]))
print("let's look at value in a[0][2] - {}".format(a[0][2]))
a[0][2] = int(input("enter new value for a[0][2]: "))
print("now a[0][2] has a value of {}\n".format(a[0][2]))
'''
a = [[1, 2, 3, 4], [11, 22, 33, 44], [99, 88, 77, 66]]
print("a = ", a)
print("\n".join([" ".join([str(a[i][j]) for j in range(len(a[i]))]) for i in range(len(a))]))
print("\n".join([" ".join([str(i) for i in row]) for row in a]))
count = 0
summ = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        summ += a[i][j]
        count += 1
print("first way: sum = {}, count = {}".format(summ, count))
count = 0
summ = 0
for row in a:
    for item in row:
        summ += item
        count += 1
print("second way: sum = {}, count = {}".format(summ, count))
_a = 1
