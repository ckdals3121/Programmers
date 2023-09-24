# visited 처리해서 그룹을 하나씩 하나씩 만들어간다

def solution(cards) :
    answer = 0
    visited = [False] * (len(cards) + 1)

    for card in cards :
        if not visited[card] :
            temp = []
            while card not in temp :
                temp.append(card)
                card = cards[card - 1]
                visited[card] = True
            
            answer.append(len(temp))
    
    if answer[0] == len(cards) :
        return 0
    else :
        answer.sort(reverse = True)
    return answer[0] * answer[1]