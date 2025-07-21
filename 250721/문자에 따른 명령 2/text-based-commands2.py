dirs = list(input())
dirc = 0
x,y=0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
#print(dirs)
for i in (dirs):
    if i =="L":
        dirc =(dirc-1)%4
    if i =="R":
        dirc =(dirc+1)%4
    if i == "F":
        x,y = x+dx[dirc],y+dy[dirc]

print(x, y)
# Please write your code here.