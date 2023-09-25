# plans 를 하나씩 순회하면서, 그 다음 plan 의 시작시간보다 끝나는 시간이 짧으면 answer 에 넣고, 멈춰 놓은 것들을 순회하고,
# 시간이 더 길면, 하던걸 stop 에 넣어두고, stop 에 넣을 때는 [name, left_time] 이런 식으로 한다

def convert_time(s) :
    h, m = map(int, s.split(':'))
    return 60 * h + m

def solution(plans) :
    answer = []
    stop = []

    plans = [(name, convert_time(start), int(playtime)) for name, start, playtime in plans]
    plans = sorted(plans, key = lambda x: x[1])

    while plans :
        if len(plans) > 1 :
            name1, start1, playtime1 = plans[0]
            _, start2, _ = plans[1]

            endTime1 = start1 + playtime1
            if endTime1 > start2 :
                stop.append([name1, endTime1 - start2])
                plans.pop(0)
            else :
                answer.append(name1)
                plans.pop(0)
                temp = start2 - endTime1
                while stop :
                    if stop[-1][1] <= temp :
                        temp -= stop[-1][1]
                        answer.append(stop.pop()[0])
                    else :
                        stop[-1][1] -= temp
                        break
        else :
            answer.append(plans.pop(0)[0])
    
    return answer + list(map(lambda x: x[0], stop[::-1]))

