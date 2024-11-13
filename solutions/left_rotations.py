def array_left_rotation(a, n, k):
    result = [0] * len(a)
    for i in range(n):
        index = (i+(n-k))%n
        #print(index)
        result[index] = a[i]  
    return result

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
