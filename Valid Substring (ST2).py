def findmax(s):
    if (len(s)<=1):
        return 0
    cmax = 0
    l = [0] * (len(s))
    for i in range(1,len(s)):
        if ((s[i]== ')' and i - l[i-1]-1 >= 0 and s[i-l[i-1]-1] == '(')):
            l[i] = l[i-1] + 2
            if (i-l[i-1]-2 >= 0):
                l[i] += (l[i-l[i-1]-2])
            else:
                l[i] += 0
            cmax = max(l[i],cmax)
    return cmax

if __name__ == '__main__':
    str = input()
    print(findmax(str))
            
        
    
