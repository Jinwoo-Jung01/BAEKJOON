import sys
from collections import deque

N = int(sys.stdin.readline())

numbers = deque()
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

num = 1
stack = []
output = []
flag = False

while(len(numbers) > 0):
    if num <= numbers[0]:
        while(num < numbers[0] + 1):
            output.append("+")
            stack.append(num)
            num += 1

    if stack[-1] == numbers[0]:
        stack.pop()
        numbers.popleft()
        output.append("-")
    else:
        flag = True
        break

if flag:
    print("NO")
else:
    for i in range(len(output)):
        print(output[i])