import sys

K = int(sys.stdin.readline())

nums = []

for i in range(K):
    num = int(sys.stdin.readline())

    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))

'''
sys.stdin.readline() 사용 법 익히기
'''