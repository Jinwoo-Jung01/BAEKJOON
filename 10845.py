import sys
from collections import deque

N=int(sys.stdin.readline())
dq = deque()

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if len(order) == 2:
        dq.append(order[1])
    
    elif order[0] == 'pop':
        print(dq.popleft() if len(dq) != 0 else -1)
    
    elif order[0] == 'size':
        print(len(dq))
    
    elif order[0] == 'empty':
        print(1 if len(dq)==0 else 0)
    
    elif order[0] == 'front':
        print(dq[0] if len(dq)!=0 else -1)

    elif order[0] == 'back':
        print(dq[-1] if len(dq)!=0 else -1)