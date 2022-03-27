def hanoi_tower(n, start, end): # n = 원판 개수, start = 시작지점, end = 목표지점
    if n == 1: # 원판 개수가 1이면 시작지점과 목표지점을 print하고 함수를 나감
        print(start, end)
        return
    hanoi_tower(n-1,start,6-start-end) #재귀를 통해 시작지점과 목표지점 그리고 보조지점을 구한다. 1번 2번 3번 막대를 다 더하면 6이므로 6에서 시작,목표를 뺀 값이 보조지점이다. 즉, 보조지점을 목표로 옮김
    print(start,end)
    hanoi_tower(n-1,6-start-end,end) # 보조지점에 옮긴 원판을 목표지점으로 옮긴다.

n = int(input())
print(2**n-1)
hanoi_tower(n,1,3)
