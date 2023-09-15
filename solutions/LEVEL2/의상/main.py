# 의상의 종류만 추출해서 list 를 만들고,
# 의상의 종류: 의상의 개수 형태인 counter 를 생성한다.
# 의상의 개수가 2개 라면, 그 의상을 안입는 경우, 1번째를 입는 경우, 2번째를 입는 경우 총 3개이다.
# 즉 의상의 개수 + 1 개가 가능하다
# 그렇게 모든 경우의 수를 곱해서 개수를 구한 후, 모든 의상을 안입는 경우 1가지를 뺀 값을 return 한다

from collections import Counter

def solution(clothes):
    answer = 1
    temp = []
    
    for clothe in clothes :
        temp.append(clothe[1])
    
    counter = Counter(temp)

    for count in counter :
        answer *= counter[count] + 1
    
    return answer - 1