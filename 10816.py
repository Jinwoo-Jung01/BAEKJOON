import sys

N = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
dict_n = {}
for i in numbers:
    if i in dict_n:
        dict_n[i] += 1
    else:
        dict_n[i] = 1

M = int(sys.stdin.readline())
find_numbers = map(int, sys.stdin.readline().split())
answer = []
for num in find_numbers:
    if num in dict_n:
        answer.append(dict_n[num])
    else:
        answer.append(0)
        
print(*answer, sep=" ")
    
'''
한줄출력방법
'''