# Enter, Leave 액션들만 따로 모으고, nickname 을 dictionary 로 따로 관리한다

def solution(records):
    answer = []
    changed_records = []
    nickname_list = {} # userid : nickname

    for record in records :
        temp = record.split()
        if temp[0] == "Enter" or temp[0] == "Leave" :
            changed_records.append((temp[0], temp[1]))
        if len(temp) == 3 :
            nickname_list[temp[1]] = temp[2]

    for record in changed_records :
        if record[0] == "Enter" :
            answer.append(nickname_list[record[1]] + "님이 들어왔습니다.")
        else :
            answer.append(nickname_list[record[1]] + "님이 나갔습니다.")
    
    return answer
