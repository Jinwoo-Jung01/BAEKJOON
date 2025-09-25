import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(sys.stdin.readline())

min_cnt = 65

for x in range(N-7):
    for y in range(M-7):

        w_cnt, b_cnt = 0, 0        

        for dx in range(8):
            for dy in range(8):
                cur = board[x+dx][y+dy]
                if (dx+dy) % 2 == 0: # cur
                    if cur != 'W': w_cnt += 1
                    if cur != 'B': b_cnt += 1
                else: # !cur
                    if cur != 'B': w_cnt += 1
                    if cur != 'W': b_cnt += 1

        min_cnt = min(min_cnt, w_cnt, b_cnt)

print(min_cnt)

'''
시작 W/B를 기준으로 확인하는 것이 아닌, 그 반대가 되는 경우도 고려
'''