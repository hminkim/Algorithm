N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
price = 0
tmpt = city[0]

for i in range(N-1):
    if tmpt < i:
        tmpt = city[i]
    price += tmpt * road[i]

print(price)