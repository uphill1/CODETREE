# t=int(input())
# n=0
# def hello_world(N):
#
#     if n==N:
#         print()
#         return
#     print(n,end=" ")
#     hello_world(n+1)
#     print(n,end=" ")
#
# hello_world(t)
N=int(input())
def print_up(N):
    if(N==0):
        return
    print_up(N-1)
    print(N,end=" ")

def print_down(N):
    if(N==0):
        return
    print(N,end=" ")
    print_down(N-1)
print_up(N)
print()
print_down(N)
