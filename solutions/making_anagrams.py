def number_needed(a, b):
    #sortA = ''.join(sorted(a))
    #sortB = ''.join(sorted(b))
    a = list(a)
    b = list(b)
    #print(a,b)
    i, j =0,0
    #pass
    #print(len(a), len(b))
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                result.append(a[i])
                result.append(b[j])
                a[i]=' '
                b[j]='0'
    #print(result)
    count = len(a) + len(b) - len(result)      
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))
