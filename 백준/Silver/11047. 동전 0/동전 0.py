K, N = map(int, input().split())
money_arr = []
count = 0
for _ in range(K):
    money_arr.append(int(input()))

money_arr.reverse()

for money in money_arr:
    if money > N:
        continue
    else:
        money_count = N // money
        N = N - money * money_count
        count += money_count

print(count)