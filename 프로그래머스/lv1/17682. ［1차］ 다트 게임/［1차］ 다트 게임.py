def solution(dartResult):
    answer = 0
    score_arr = []
    tmpt_num = 0

    for idx, i in enumerate(dartResult):
        # 숫자일 때 기준이 되는 점수
        if i.isdigit():
            if dartResult[idx-1].isdigit():
                tmpt_num = int(str(tmpt_num) + i)
            else:
                tmpt_num = int(i)
        else:
            # 싱글일 때
            if i == "S":
                score_arr.append(tmpt_num ** 1)
            # 더블일 때
            elif i == "D":
                score_arr.append(tmpt_num ** 2)
            # 트리플일 때
            elif i == "T":
                score_arr.append(tmpt_num ** 3)
            else:
                # 스타상일 때
                if i == "*":
                    if len(score_arr) > 1:
                        score_arr[-1] = score_arr[-1] * 2
                        score_arr[-2] = score_arr[-2] * 2
                    else:
                        score_arr[-1] = score_arr[-1] * 2
                # 아차상일 때
                elif i == "#":
                    score_arr[-1] = score_arr[-1] * -1

    answer = sum(score_arr)
    return answer