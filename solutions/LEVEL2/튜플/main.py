# 집합의 개수를 key 로 해서 정렬한 sorted_sets 를 만든다
# 개수가 1개인 집합의 원소는 무조건 첫번째 원소이다. 개수가 2개인 집합에는 첫번째 원소가 포함되어 있을 것이므로, 나머지 원소가 두번째 원소가 된다.
# 위의 로직을 계속 반복한다

def solution(s):
    answer = []
    stripped_str = s.strip('{}')
    set_strs = stripped_str.split('},{')
    sets_list = [set(map(int, s.split(','))) for s in set_strs]
    sorted_sets = sorted(sets_list, key = len)
    
    for sset in sorted_sets :
        for item in sset :
            if item not in answer :
                answer.append(item)
                break
    return answer