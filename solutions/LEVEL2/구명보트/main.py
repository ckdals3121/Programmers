# 사람을 몸무게순으로 정렬한다. 젤 무거운 사람은, 남아있는 젤 가벼운 사람과 들어가거나, limit 을 넘기면 혼자 타야만 한다.
# 젤 무거운 사람과 젤 가벼운 사람이 함께 타야 젤 호율적이다

def solution(people, limit):
    answer = 0
    
    people.sort()
    left = 0
    right = len(people) - 1
    
    while left < right :
        if people[left] + people[right] > limit :
            right -= 1
        elif people[left] + people[right] <= limit :
            answer += 1
            left += 1
            right -= 1
    
    answer += (len(people) - 2 * answer)
        
    return answer