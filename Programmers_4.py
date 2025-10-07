## =============== 코딩테스트 연습 > PCCP 기출문제 > [PCCP 기출문제] 2번 / 석유 시추 ===============

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    dict_str = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    for dt in data:
        if dt[dict_str[ext]] < val_ext:
            answer.append(dt)
    
    answer.sort(key=lambda x: x[dict_str[sort_by]])
    
    return answer

'''
2차원 list에서 특정 원소 기준으로 오름차순 정렬하는 방법 익히기
'''