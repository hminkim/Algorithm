import heapq

n = int(input())

gift = []

for _ in range(n):
    a = list(map(int, input().split()))
    # 아이를 만났을 때
    if a[0] == 0 :
        # 선물이 없으면
        if len(gift) == 0:
            print(-1)
        # 선물이 있으면
        else:
            print(-heapq.heappop(gift))
    # 선물을 충전할 때
    else:
        for i in range(1, a[0]+1):
            heapq.heappush(gift, -a[i])