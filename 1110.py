N = int(input())
cnt = 0
origin = N
after = N

while(1):
    x = after//10
    y = after%10
    after = y*10 + (x+y)%10
    cnt += 1

    if origin == after:
        break

print(cnt)

'''
쉽다
'''
