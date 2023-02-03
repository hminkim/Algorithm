N = int(input())
meeting = []

for i in range(N):
    meeting.append(list(map(int, input().split())))

# 끝나는 시간을 1번째 기준, 시작 시간을 2번째 기준으로 정렬
meeting = sorted(meeting, key = lambda a : (a[1], a[0]))

last_end = 0
count = 0

for start, end in meeting:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
