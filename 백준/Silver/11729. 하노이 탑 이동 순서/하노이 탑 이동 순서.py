N = int(input())
hanoi_arr = []

def hanoi(N, start, to, via):
    if N == 1:
        hanoi_arr.append((start, to))
    else:
        hanoi(N-1, start, via, to)
        hanoi_arr.append((start, to))
        hanoi(N-1, via, to, start)

    return hanoi_arr

hanoi(N, 1, 3, 2)

print(len(hanoi_arr))
for i in hanoi_arr:
    print(i[0], i[1])