N = int(input("enter the  number of elements in the array : "))  
arr = [input().strip() for _ in range(N)]   

for i in range(N):  
    niceness = 0     
    for j in range(i):   
        if arr[j] < arr[i]:   
            niceness += 1     
    print(niceness)   
