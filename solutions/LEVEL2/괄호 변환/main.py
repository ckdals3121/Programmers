# 올바른 괄호인지는 stack을 활용한다
# 주어진 알고리즘 대로 코드를 작성한다

def seperate(p) :
    left = right = 0
    for i in range(len(p)) :
        if p[i] == "(" :
            left += 1
        else :
            right += 1
        if left == right :
            return p[:i + 1], p[i + 1:]

def isCorrect(p) :
    stack = []
    for i in range(len(p)) :
        if p[i] == "(" :
            stack.append(p[i])
        else :
            if not stack :
                return False
            stack.pop()
    if stack :
        return False
    else :
        return True

def solution(p):
    answer = ''
    if len(p) == 0 :
        return p
    
    u, v = seperate(p)
    
    if isCorrect(u) :
        return u + solution(v)
    else :
        answer = "("
        answer += solution(v)
        answer += ")"
        
        for i in range(1, len(u) - 1) :
            if u[i] == "(" :
                answer += ")"
            else :
                answer += "("
        return answer
        
        
    return answer