## =============== 코딩테스트 연습 > PCCP 기출문제 > [PCCP 기출문제] 1번 / 붕대 감기 ===============

def solution(bandage, health, attacks):
    answer = 0
    cnt_atk = 0
    cnt_continue = 0
    cur_health = health
    
    for i in range(1, attacks[-1][0]+1):
        if attacks[cnt_atk][0] == i:
            cnt_continue = 0
            cur_health -= attacks[cnt_atk][1]
            if cur_health <= 0:
                answer = -1
                return answer
            
            cnt_atk += 1
        else:
            cnt_continue += 1
            cur_health = min(health, cur_health+bandage[1])
            if cnt_continue == bandage[0]:
                cnt_continue = 0
                cur_health = min(health, cur_health+bandage[2])

    answer = cur_health
    
    return answer