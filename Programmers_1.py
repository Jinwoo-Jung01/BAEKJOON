## =============== 코딩테스트 연습 > 연습문제 > 과제진행하기 ===============

## Accuracy: 45.8%
'''
조금 단순하게 생각 해 보자.
'''
# from collections import deque

# def solution(plans):
#     answer = []
        
#     # 우선순위는 새로 시작해야 하는 과제임(시간에 따라 진행)
#     # 여러개의 멈춘 과제가 있을 경우 최근에 멈춘 과제부터 시작
#     # 진행중이던 과제가 끝나는 시각과 새로운 과제를 시작해야하는 시각이 같은 경우 진행중이던 과제는 끝난 것으로 판단합니다.

#     dict_plan = {}
#     dq = deque()
    
    
#     for plan in plans:
#         a,b,c = plan
#         m, s = map(int, b.split(":"))
#         tmp = m*60+s
#         dict_plan[a] = (tmp, int(c))
    
#     # 이거 활용 방법 기억할 것
#     sorted_plan = sorted(dict_plan.items(), key=lambda x: x[1][0])
#     todo = []
#     now = sorted_plan[0][1][0]
#     idx = 0
    
#     while(len(answer) != len(plans)):

#         if idx+1 != len(plans):
#             if now + sorted_plan[idx][1][1] > sorted_plan[idx+1][1][0]:   # 진행 중인 과제 시간 초과
#                 todo.append([sorted_plan[idx][0],sorted_plan[idx][1][1]-(sorted_plan[idx+1][1][0]-now)])
#                 now = sorted_plan[idx+1][1][0]
#                 idx += 1
#                 continue
#             else:
#                 now += sorted_plan[idx][1][1]
#                 answer.append(sorted_plan[idx][0])
#                 idx += 1
#         else:
#             now += sorted_plan[idx][1][1]
#             answer.append(sorted_plan[idx][0])
            
#             for i in range(len(todo)-1, -1, -1):
#                 answer.append(todo[i][0])
                
#             break
                
#         for i in range(len(todo)-1, -1, -1):
#             if todo[i][1] == 0:
#                 continue
            
#             if now + todo[i][1] > sorted_plan[idx][1][0]:
#                 todo[i][1] -= (sorted_plan[idx][1][0]-now)
#                 now = sorted_plan[idx][1][0]
#                 break
#             else:
#                 now += todo[i][1]
#                 todo[i][1]=0
#                 answer.append(todo[i][0])
        
#     return answer


## Accuracy: 100%
def solution(plans):
    stack = []
    answer = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    
    for i in range(len(plans)-1):   # 마지막 과제는 무조건 가장 먼저 실행되어야 함
        stack.append([plans[i][0], plans[i][2]])    # 과제의 시작 시간은 더이상 필요 없음
        gap = plans[i+1][1] - plans[i][1]
        
        while stack and gap:
            if stack[-1][1] <= gap: # 다음 과제 시작 전에 이전 과제 수행 가능
                subject, time = stack.pop()
                gap -= time
                answer.append(subject)
            else:   # gap 만큼만 이전 과제 수행 이후 다음 과제 수행
                stack[-1][1] -= gap
                gap = 0
                
    answer.append(plans[-1][0])
    for i in range(len(stack)): 
        answer.append(stack[~i][0]) # 마지막 원소부터 접근할 수 있는 방법
        
    return answer