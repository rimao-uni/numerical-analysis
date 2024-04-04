"""
2022-11-22
https://atcoder.jp/contests/abc007/tasks/abc007_3
幅優先探索による最短経路探索
"""


from collections import deque

R,C  = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx =  map(int,input().split())
c = [list(input()) for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

que = deque()
que.append([sy,sx])

visited = [[0 for i in range(C)] for j in range(R)] #訪れた記録
dist = [[-1 for i in range(C)] for j in range(R)] #距離を記録
visited[sy][sx] = 1
dist[sy][sx] = 0

while len(que)>0:
    y,x = que.popleft()

    for y_move,x_move in [[-1,0],[1,0],[0,1],[0,-1]]:   #4方向の行き先
        ny = y + y_move
        nx = x + x_move

        if visited[ny][nx] == 1 or c[ny][nx]=="#":
            continue

        # if length[ny][nx] > length[y][x]+1:   #距離
        dist[ny][nx] = dist[y][x] + 1

        visited[ny][nx] = 1
    
        que.append([ny,nx])  #.のときqueに入れる

for i in range(R):
    for j in range(C):
        if c[i][j] == "#":
            continue


        c[i][j] = dist[i][j]

#出力
for i in range(R):
    for j in range(C):
        print(c[i][j],end=' ')
    print("")

    
