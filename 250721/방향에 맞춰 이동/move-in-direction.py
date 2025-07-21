n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
x, y = 0,0
dx = [1,-1,0,0]
dy= [0,0,-1,1]

for i in range(n):
    dirc, dist = tuple(input().split)

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
