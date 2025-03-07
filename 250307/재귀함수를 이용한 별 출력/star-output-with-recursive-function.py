
n=int(input())
def print_up(n):
    if(n==0):
        return
    print_up(n-1)
    print("*"*n)

# def print_down(N):
#     if(N==0):
#         return
#     print(N,end=" ")
#     print_down(N-1)
print_up(n)

