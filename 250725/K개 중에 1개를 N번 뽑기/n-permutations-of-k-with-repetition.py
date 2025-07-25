K, N = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()
# Please write your code here.
"""
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                for e in range(1,4):
                    print(a,b,c,d,e)

#근데 이건 숫자가 바뀔때 마다 달라짐
"""

##
#각자의 역할을 충실히 하다 
#0과 1을 골라서 다음 스텝으로 넘긴다.
#choose는 내 위치를 채우고 그 다음으로 넘긴다 
def choose(curr_num):
    if curr_num == N+1:
        print_answer()
        return
    for i in range(1,K+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()
    return

    
choose(1)