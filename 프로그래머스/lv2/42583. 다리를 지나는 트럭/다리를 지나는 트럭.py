from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 1
    bridge = deque()
    
    for i in range(bridge_length):
        bridge.append(0)
    
    bridge_weight = 0
    while len(truck_weights) !=0 :
        bridge_weight -= bridge.popleft()
        
        if bridge_weight+truck_weights[0] > weight:
            bridge.append(0)
        else :
            bridge.append(truck_weights[0])
            bridge_weight += truck_weights[0]
            
            truck_weights= truck_weights[1:]  
        time +=1
    time += bridge_length-1
    
    
    return time