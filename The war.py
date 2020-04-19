string = list((input().replace('x', ',')).split())
rows = int(string[0])
columns = int(string[-1])
digonal= rows * columns
count = 0
for i in range(rows):
    for j in range(columns):
        if (i+j)%2 == 0:
            count += 1
print(digonal-count)
