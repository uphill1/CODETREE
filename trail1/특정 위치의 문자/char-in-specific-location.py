list=["L","E","B","R","O","S"]
str = input()
find =False
for i in range(6):
    if list[i]==str:
        print(i)
        find=True
    
if not(find):
    print("None")
