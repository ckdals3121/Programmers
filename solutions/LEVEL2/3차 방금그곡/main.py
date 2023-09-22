# 음계 1개가 1문자로 표현되게 만든다
# 코드를 재생된 시간만큼 이어 붙여서 재생성 한다
# 그런 다음 m이 포함된 코드를 순회하면서 찾고, answer를 업데이트한다

def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')
    
    for musicinfo in musicinfos :
        start, end, title, code = map(str, musicinfo.split(","))
        start_hour, start_time = map(int, start.split(":"))
        end_hour, end_time = map(int, end.split(":"))
        
        time = 60 * (end_hour - start_hour) + (end_time - start_time)

        code = code.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')
        
        code = code * ((time // len(code)) + 1)
        code = code[:time]

        
        if m in code :
            if answer == None or answer[0] < time or (answer[0] == time and answer[1] > start_hour * 60 + start_time) :
                answer = (time, start_hour * 60 + start_time, title)
                
    if answer == None :
        return "(None)"
    return answer[2]