# A 를 오름차순, B 를 내림차순으로 정렬 후, 같은 인덱스끼리 값을 곱해서 더함

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
        
    for i in range(len(A)) :
        answer += A[i] * B[i]
        
    return answer