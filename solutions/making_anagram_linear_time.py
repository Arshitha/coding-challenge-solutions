def number_needed(a, b):
    count = 0
    freq = [0]*26
    
    for i in range(len(a)):
        ind1 = ord(a[i]) - ord('a')  #the ord() function converts a char to it's ascii value
        freq[ind1] += 1
        
    for j in range(len(b)):
        ind2 = ord(b[j]) - ord('a')
        freq[ind2] -= 1
    
    for each in freq:
        #print (each)
        count += abs(each)
             
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))
