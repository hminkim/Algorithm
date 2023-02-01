from itertools import combinations

def solution(number):
    answer = 0
    trio = list(combinations(number, 3))

    for i in trio:
        sum = 0
        for j in i:
            sum += j
        if sum == 0:
            answer += 1

    return answer