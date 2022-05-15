n = int(input())

visited = [False for _ in range(n)] #n만큼 false를 만든다.
startlink = [list(map(int,input().split())) for _ in range(n)]
minnum = 1000000000

def dfs(depth, index):
    global minnum
    if depth == n//2:
        start, link  = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += startlink[i][j]
                elif not visited[i] and not visited[j]:
                    link += startlink[i][j]
        minnum = min(minnum,abs(start-link))
        return

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False

dfs(0,0)
print(minnum)