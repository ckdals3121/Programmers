# 연산자의 우선순위로 가능한 경우의 수를 모두 구하고, 각 격우마다 계산을 해서 최대값을 찾는다

from itertools import permutations

def calculate(exp, ops) :
    exp_list = []
    num = ''
    
    for i in range(len(exp)) :
        if exp[i].isdigit() :
            num += exp[i]
        else :
            exp_list.append(num)
            exp_list.append(exp[i])
            num = ''
    exp_list.append(num)
    
    for op in ops :
        stack = []
        while len(exp_list) != 0 :
            temp = exp_list.pop(0)
            if temp == op :
                result = eval(str(stack.pop()) + op + str(exp_list.pop(0)))
                stack.append(result)
            else :
                stack.append(temp)
        exp_list = stack
    
    return abs(int(stack[0]))
        
    
def solution(expression):
    ops = ['-', '+', '*']
    ops = list(permutations(ops, 3))
    
    answer = 0
    for op in ops :
        answer = max(answer, calculate(expression, op))
    return answer