import sys

pos_k, pos_r, N = sys.stdin.readline().split()
N =int(N)

w_k, h_k = pos_k[0], pos_k[1]
w_k = ord(w_k) - ord('A')
h_k = 8-int(h_k)

w_r, h_r = pos_r[0], pos_r[1]
w_r = ord(w_r) - ord('A')
h_r = 8-int(h_r)

move = {}
move["R"] = (0, 1)
move["L"] = (0, -1)
move["B"] = (1, 0)
move["T"] = (-1,0)
move["RT"] = (-1, 1)
move["LT"] = (-1, -1)
move["RB"] = (1, 1)
move["LB"] = (1, -1)


for i in range(N):
    movement = move[input()]
    if h_k + movement[0] == h_r and w_k + movement[1] == w_r:   # king이 rock을 잡음
        if h_r + movement[0] >=0 and h_r + movement[0] < 8 and w_r + movement[1] >=0 and w_r + movement[1] < 8:
            h_r += movement[0]
            w_r += movement[1]
            h_k += movement[0]
            w_k += movement[1]
    
    else:
        if h_k + movement[0] >=0 and h_k + movement[0] < 8 and w_k + movement[1] >=0 and w_k + movement[1] < 8:
            h_k += movement[0]
            w_k += movement[1]


w_k = chr(w_k + ord('A'))
h_k = 8-h_k
king = w_k + str(h_k)
print(king)

w_r = chr(w_r + ord('A'))
h_r = 8-h_r
rock = w_r + str(h_r)
print(rock)

'''
체스판 -> 배열 할당
'''