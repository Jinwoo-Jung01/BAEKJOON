import sys

N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(numbers)/N))

# 중앙값
numbers.sort()
print(numbers[N//2])

num_dict = {}
for i in range(N):
    if numbers[i] in num_dict:
        num_dict[numbers[i]] += 1
    else:
        num_dict[numbers[i]] = 1

# 최빈값(여러 개일 경우 모두)
max_freq = max(num_dict.values())
most_frequent = [k for k, v in num_dict.items() if v == max_freq]
most_frequent.sort()
print(most_frequent[1] if len(most_frequent) > 1 else most_frequent[0])

# 범위
min_num = numbers[0]
max_num = numbers[-1]
print(max_num-min_num)

'''
dictionary key 기반 정렬
'''