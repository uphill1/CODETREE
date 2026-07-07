n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.
max=0

for i in range(n-3+1):
    for j in range(n-3+1):
        sum=0
        for k in range(3):
            for l in range(3):
                sum+=grid[i+k][j+l]
        if max<sum:
            max=sum

print(max)