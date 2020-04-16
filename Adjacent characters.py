n = input()
if len(n)<100:
    if len(n)%2==1:
        print('Odd length.')
    else:
        t = list(n)
        t[::2], t[1::2] = t[1::2], t[::2]
        print(''.join(t))
