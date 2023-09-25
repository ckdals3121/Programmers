# 5개씩 끊은 후, diamond, iron, rocks 의 개수를 새고, diamond, iron, rocks 순으로 key 지정 sort를 한다.
# 그 다음 diamond, iron, rocks 곡괭이 순으로 광물을 캐 준다
# 다이아가 많은걸 다이아로 캐야 최소로 할 수 있다

def solution(picks, minerals):
    answer = 0

    minerals = minerals[: sum(picks) * 5]
    minerals = [minerals[i: i + 5] for i in range(0, len(minerals), 5)]

    costs = []

    for mineral in minerals :
        cnt = [0, 0, 0]
        for m in mineral :
            if m == 'diamond' :
                cnt[0] += 1
            elif m == 'iron' :
                cnt[1] += 1
            else :
                cnt[2] += 1
        costs.append(cnt)
    
    costs = sorted(costs, key = lambda x: (-x[0], -x[1], -x[2]))

    for cost in costs :
        if picks[0] > 0 :
            picks[0] -= 1
            answer += sum(cost)
        elif picks[1] > 0 :
            picks[1] -= 1
            answer += cost[0] * 5 + cost[1] + cost[2]
        elif picks[2] > 0 :
            picks[2] -= 1
            answer += cost[0] * 25 + cost[1] * 5 + cost[2]
        else :
            break
            
    return answer