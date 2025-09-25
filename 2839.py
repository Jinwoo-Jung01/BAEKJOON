input = int(input())

if input % 5 == 0:                  # 5로 나누어 떨어짐: 가장 적은 설탕 사용
    print(input//5)
else:
    cnt = 0

    while input>0:
        input -= 3
        cnt += 1

        if input % 5 == 0:          # 3과 5의 조합으로 나누어 떨어짐
            cnt += input // 5
            print(cnt)
            break
        
        elif input == 0:            # 3의 배수
            print(cnt)
            break
    
        elif input == 1 or input == 2:  # 3과 5의 조합으로 구할 수 없음
            print(-1)
            break


'''
최소 봉지 사용하는 것이 조건이므로 5로 최대한 담고, 안되면 3으로 담는 것이라고 생각해야 됨
'''