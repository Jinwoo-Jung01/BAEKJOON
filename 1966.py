import sys
from collections import deque

loop = int(sys.stdin.readline())
for _ in range(loop):
    N, M = list(map(int, sys.stdin.readline().split()))
    weights = list(map(int, sys.stdin.readline().split()))
    dq = deque()
    cnt = 0

    for i in range(len(weights)):
        dq.append((weights[i], i))

    if N == 1:
        print(1)
    else:
        while(len(dq) > 0):
            base = dq[0][0]
            flag = False
            
            for i in range(1, len(dq)):
                if dq[i][0] > base:
                    flag = True
            
            if flag:
                dq.append(dq.popleft())
            else:
                out = dq.popleft()
                cnt+=1
                if out[1] == M:
                    print(cnt)
                    break


'''
map 활용 방법
'''