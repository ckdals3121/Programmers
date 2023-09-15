# 처음과 끝이 연결되어 있는 것을 표현하기 위해, 원래 리스트의 끝에 다시 리스트를 붙여 넣는다
# 가능한 모든 합을 set 에 집어 넣는다. set 이기 때문에 중복은 알아서 제거된다

def solution(elements):
    values = set()

    elements = elements + elements
    
    for i in range(1, len(elements) // 2 + 1) :
        for j in range(len(elements) // 2) :
            values.add(sum(elements[j: j + i]))
            
    return len(values)