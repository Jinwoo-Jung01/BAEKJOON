## =============== 코딩테스트 연습 > PCCP 기출문제 > [PCCP 기출문제] 2번 / 석유 시추 ===============

from collections import deque

def solution(land):
    answer = 0
    max_num = 0
    
    # bfs로 잡고 풀면 될 듯!
    
    h = len(land)
    w = len(land[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0]*w for _ in range(h)]
    
    # 석유 그룹이 다른 열에도 속해있을 수도 있으므로 그에 대한 처리가 필요
    oil_sum = [0]*w

    def bfs(pos):
        x, y = pos
        visited[y][x] = True
        count = 1

        dq = deque()
        dq.append(pos)
        
        cols = set([x])
        
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                xx, yy = x+dx[i], y+dy[i]
                
                # 아직 방문하지 않은 석유
                if (0 <= xx < w) and (0 <= yy < h) and visited[yy][xx] == False and land[yy][xx] == 1:
                    dq.append((xx, yy))
                    visited[yy][xx] = True
                    count += 1
                    cols.add(xx)
        
        for col in cols:
            oil_sum[col] += count
                    
    
    for x in range(w):
        for y in range(h):
            if land[y][x] == 1 and not visited[y][x]:
                bfs((x, y))
    
    return max(oil_sum)

'''
단순한 bfs가 아니라, 이미 방문했더라도 석유 그룹이 다른 열에 속해있을 수 있으므로 이를 고려해야 한다.
'''