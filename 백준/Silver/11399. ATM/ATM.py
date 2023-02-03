N = int(input())
people = list(map(int, input().split()))
waiting_time = 0
waiting_time_arr = []

while people:
    min_withdraw_time = min(people)
    people.remove(min_withdraw_time)
    waiting_time += min_withdraw_time
    waiting_time_arr.append(waiting_time)

print(sum(waiting_time_arr))