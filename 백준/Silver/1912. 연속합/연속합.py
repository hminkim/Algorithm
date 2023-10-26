n = int(input())
list = list(map(int, input().split()))
answer_list = [0] * n

for idx in range(0, n):
    if idx == 0:
        answer_list[idx] = list[idx]
    else:
        answer_list[idx] = max(list[idx], answer_list[idx-1] + list[idx])

print(max(answer_list))