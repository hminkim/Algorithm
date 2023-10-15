def solution(sequence, k):
    answer = []
    idx1 = 0
    idx2 = 0
    temp = sequence[0]
    length = 1000001

    while idx1 <= idx2 and idx2 < len(sequence):
        if temp == k :
            if idx2 - idx1 + 1 < length :
                length = idx2 - idx1 + 1
                answer = [idx1, idx2]
            temp -= sequence[idx1]
            idx1 += 1

        elif temp < k :
            idx2 += 1
            if idx2 < len(sequence) :
                temp += sequence[idx2]

        elif temp > k :
            temp -= sequence[idx1]
            idx1 += 1

    return answer