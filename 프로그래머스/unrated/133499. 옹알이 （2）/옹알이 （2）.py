def solution(babbling):
    answer = 0
    re_answer = 0
    tmpt_arr = []

    # 주어진 발음을 정수로 치환
    for idx in range(len(babbling)):
        babbling[idx] = babbling[idx].replace("aya", "1")
        babbling[idx] = babbling[idx].replace("ye", "2")
        babbling[idx] = babbling[idx].replace("woo", "3")
        babbling[idx] = babbling[idx].replace("ma", "4")

    # 주어진 발음으로만 이루어져 모두가 치환된 발음
    for i in babbling:
        if i.isdigit():
            tmpt_arr.append(i)

    #연속된 발음이 있는지 체크
    for j in tmpt_arr:
        for idx, k in enumerate(j):
            if idx > 0 and k == j[idx-1]:
                re_answer += 1
                break

    answer = len(tmpt_arr) - re_answer

    return answer