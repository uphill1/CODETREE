
n=int(input())
def print_up(n):
    if(n==0):
        return
    print_up(n-1)
    print("* " * n)

def print_down(n):
    if(n==0):
        return
    print("* " * n)
    print_down(n-1)
print_down(n)
print_up(n)

