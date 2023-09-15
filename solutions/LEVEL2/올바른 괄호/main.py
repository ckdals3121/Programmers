# stack을 활용해서 ( 는 insert 하고, ) 가 나오면 pop 함
# 괄호가 열린 다음에 닫혀야 하기 때문에 어느 순간에도 닫힌 괄호의 개수가 열린 괄호의 개수보다 많으면 안됨
# 열린괄호와 닫힌괄호의 개수는 같아야 함

def solution(s):
    stack = []
    
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append(s[i])
        else :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
    
    if len(stack) == 0 :
        return True
    else :
        return False