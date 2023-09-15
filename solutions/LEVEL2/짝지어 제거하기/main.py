# 문자를 1개씩 stack 에 넣고, stack 에 마지막 값과 넣을 값이 같으면, pop()

def solution(s):
    stack = []

    for i in range(len(s)) :
        if len(stack) == 0 :
            stack.append(s[i])
        elif stack[-1] == s[i] :
            stack.pop()
        else :
            stack.append(s[i])

    if len(stack) == 0 :
        return 1
    else :
        return 0