from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    max_win = 0
    dices = []
    answer_dices = []
    dices_set = set(list(range(len(dice))))
    
    for i in list(combinations(dices_set,len(dice)//2)):
        dices.append([[dice[a] for a in i], [dice[b] for b in dices_set - set(i)]])
    
    for a_dice, b_dice in dices:
        sum_a = [sum(p) for p in product(*a_dice)]
        sum_b = sorted([sum(p) for p in product(*b_dice)])
        wins = sum(bisect_left(sum_b,a_s) for a_s in sum_a)
        
        if wins > max_win:
            max_win = wins
            answer_dices = a_dice
        
    answer = [dice.index(i) + 1 for i in answer_dices]
    return answer