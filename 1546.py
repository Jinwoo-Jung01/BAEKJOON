N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

sum_scores = 0
for i in range(N):
    sum_scores += scores[i]/M*100

print(sum_scores/N)

'''
주어진 데로 풀면 됨
'''