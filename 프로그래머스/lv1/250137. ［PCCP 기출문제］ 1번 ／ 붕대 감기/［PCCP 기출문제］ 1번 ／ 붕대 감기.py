def solution(bandage, health, attacks):
    prev_attack_time = 0
    current_health = health
    continue_band = 0
    
    for attack in attacks:
        continue_band = attack[0] - prev_attack_time - 1
        if continue_band//bandage[0] > 0:
            current_health += continue_band * bandage[1] + bandage[2]*(continue_band//bandage[0])
        else:
            current_health += continue_band * bandage[1]
        current_health = min(current_health, health)
        continue_band = 0
        prev_attack_time = attack[0]
        current_health -= attack[1]
        
        if current_health <= 0:
            return -1
    return current_health