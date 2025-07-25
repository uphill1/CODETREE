K, N = map(int, input().split())

# Please write your code here.
#curr_num ==1 or answer[-1]!=0이 핵심 조건 
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()
# Please write your code here.

##
#각자의 역할을 충실히 하다 
#0과 1을 골라서 다음 스텝으로 넘긴다.
#choose는 내 위치를 채우고 그 다음으로 넘긴다 
def choose(curr_num):
    if curr_num == N+1:
        print_answer()
        return
    for i in range(1,K+1):
        if len(answer)>=2 and answer[-1]==i and  answer[-2]==i: #왜 아웃오브레인지
            continue         
        answer.append(i)
        choose(curr_num+1)
        answer.pop()
    return

    
choose(1)