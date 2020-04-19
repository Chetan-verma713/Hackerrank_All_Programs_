string = ''.join((input().split()))
node = int(input())
count = int(input())
for i in range(count):
    for j in range(node-1, len(string)):
        print(string[j], end = '__')
    for k in range(0,node-1):
        print(string[k], end = '__')
