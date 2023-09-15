# 행렬곱 하는 법을 그대로 구현했다

def solution(arr1, arr2):
    answer = []
    
    for arr in arr1 :
        L = []
        
        for dx in range(len(arr2[0])) :
            sum = 0
            for dy, num in enumerate(arr) :
                sum += num * arr2[dy][dx]
            L.append(sum)
        answer.append(L)
    return answer