import sys

N = int(sys.stdin.readline())
papaer = [[0]*101 for _ in range(101)] 

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for dx in range(10):
        for dy in range(10):
            if papaer[y+dy][x+dx] != 1:
                papaer[y+dy][x+dx] = 1

cnt = 0                
for x in range(1, 101):
    for y in range(1, 101):
        if papaer[y][x] == 1:
            cnt += 1

print(cnt)