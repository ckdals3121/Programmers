# stack 을 활용해서 제대로된 괄호인지 판단하는 함수 is_good 을 만든다.
# s 를 2번 이어 붙인 후 , s의 원래 길이만큼 자르면, s를 이동시킨 것과 같다

def is_good(s) :
    stack = []
    answer = {']': '[', ')': '(', '}': '{'}
    for i in range(len(s)) :
        if s[i] == '(' or s[i] == '{' or s[i] == '[' :
            stack.append(s[i])
        else :
            if len(stack) == 0 :
                return False
            elif answer[s[i]] == stack[-1] :
                stack.pop()
            else :
                return False
    
    if len(stack) == 0 :
        return True

def solution(s):
    answer = 0
    
    length = len(s)
    
    s = s + s
    print(s)
    
    for i in range(length) :
        temp = s[i: i + length]
        if is_good(temp) :
            answer += 1
            
    return answer