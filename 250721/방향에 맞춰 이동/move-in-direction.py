n = int(input())
x, y = 0,0
dx = [1,-1,0,0]
dy= [0,0,-1,1]

for i in range(n):
    dirc, dist = tuple(input().split())
    dist = int(dist)

    if dirc == "E":
        move=0
    elif dirc == "W":
        move=0
    elif dirc == "S":
        move=0
    elif dirc == "N":
        move=0

    x= x + dx[move]*dist
    y = y+ dy[move]*dist

print(x,y)
