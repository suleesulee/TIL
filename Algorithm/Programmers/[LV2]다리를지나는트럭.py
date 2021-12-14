def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_sum = 0
    bridge = [0] * bridge_length
    second = 0
    
    # 대기트럭을 올릴수 있는지 계산
    # 대기트럭을 올리며 길이+1
    
    
    while bridge:
        bridge_sum -= bridge.pop(0)
        second += 1
        
        if truck_weights:
            if bridge_sum + truck_weights[0] > weight:
                bridge.append(0)
            else:
                tmp = truck_weights.pop(0)
                bridge.append(tmp)
                bridge_sum += tmp
                #print(bridge_sum)
    
    #print(second)
    
    return second