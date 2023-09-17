# 순서가 있는 스킬을 queue 에 넣고 비교하면서 순서가 지켜지는지 확인한다

from queue import Queue

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees :
        q = Queue()
        for i in range(len(skill)) :
            q.put(skill[i])
        if all(ch == q.get() if ch in skill else True for ch in skill_tree):
            answer += 1
    
    return answer