import sys

X = int(sys.stdin.readline())
start_num = 0

for i in range(1, 1000000):
    if start_num + i >= X:
        break
    start_num += i

delta = X-start_num
if i % 2 == 0:  # 짝수: 분자시작
    print(f"{delta}/{i-delta+1}")
else:
    print(f"{i-delta+1}/{delta}")

'''
몇개 해 보고 규칙 찾기
'''