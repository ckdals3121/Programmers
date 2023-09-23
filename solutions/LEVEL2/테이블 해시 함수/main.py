# 문제에 주어진 알고리즘대로 한다
# 1. 정렬, 2. mod 값 더하기, 3. XOR 연산 해서 더하기

def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x: [x[col - 1], x[0] * -1])
    
    for i in range(row_begin, row_end + 1) :
        temp = 0
        
        for j in data[i - 1] :
            temp += (j % i)
        
        answer ^= temp
    return answer