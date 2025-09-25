N = int(input())   # 1
arr = [input().strip() for _ in range(N)]   # 2

for i in range(N):   # 3
    niceness = 0     # 4
    for j in range(i):   # 5
        if arr[j] < arr[i]:   # 6
            niceness += 1     # 7
    print(niceness)   # 8
