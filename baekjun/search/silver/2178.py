from collections import deque

N, M = map(int, input().split())

miro = []
for i in range(N):
    miro.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))
    
    return miro[N-1][M-1]

print(bfs())