def check(answer):
    for i in range(len(answer)):
        x, y, a = answer[i]

        if a == 0:
            # 기둥
            if 0 == y or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                # 기둥은 바닥 위에 있거나 (X) => 기둥은 바닥에 있거나
                continue
        elif a == 1:
            # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
        return False

    return True


def solution(n, build_frame):
    answer = []
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 0:
            print(answer)
            answer.remove([x, y, a])
            if check(answer) == False:
                answer.append([x, y, a])
        elif b == 1:
            print(answer)
            answer.append([x, y, a])
            if check(answer) == False:
                answer.remove([x, y, a])
    answer.sort()
    return answer

# print(solution(5, 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))