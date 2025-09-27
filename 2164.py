# ===== 시간초과 =======
# import sys 

# N = int(sys.stdin.readline())

# stack = [i for i in range(1,N+1)]

# while(1):

#     stack.pop(0)
#     num = stack.pop(0)
#     stack.append(num)

#     if len(stack) == 1:
#         print(stack[0])
#         break

import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque([i for i in range(1, N+1)])

while(len(dq) > 1):
    dq.popleft()
    
    num = dq.popleft()
    dq.append(num)

print(dq[0])

'''
pop(0)보다 deque를 사용하는 것이 더 효과적이고 시간 초과가 발생하지 않는다
'''