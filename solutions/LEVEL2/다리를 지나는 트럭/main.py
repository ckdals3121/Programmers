# (시작 지점) (다리) (끝 지점)
# 이라고 할 때, 계속해서 오른쪽 으로 이동하는 게 기본 베이스이며, 시작지점에 있는 트럭이 다리위로 올라가도 다리가 버티면 올리고 그렇지 않으면 안올린다 

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0 for _ in range((bridge_length))]
    bridge_weight = 0
    
    while (on_bridge) :
        answer += 1
        bridge_weight -= on_bridge.pop(0)
        if len(truck_weights) != 0 :
            if bridge_weight + truck_weights[0] <= weight :
                bridge_weight += truck_weights[0]
                on_bridge.append(truck_weights.pop(0))
                
            else :
                on_bridge.append(0)
    return answer