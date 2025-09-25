word = input().strip().upper()  # 대소문자 구분x -> 모두 대문자로 변경
counts = {}

for ch in word:
    counts[ch] = counts.get(ch, 0) + 1  # dict에서 key의 value를 가져오는 코드(default: 0)

max_count = max(counts.values())

most_common = [ch for ch, cnt in counts.items() if cnt == max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])

'''
dictionary 사용 방법
'''