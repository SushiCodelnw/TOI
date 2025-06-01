n, m = map(int, input().split())
k = int(input())

g = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    g[x][y] += 1
    
d = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1), ( 0, 1),
              ( 1, -1), ( 1, 0), 
              ( 1, 1)]

m_p = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            count = 0
            for dx, dy in d:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    count += g[ni][nj]
            m_p = max(m_p, count)

print(m_p)