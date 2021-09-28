# 기둥과 보

def check_build(answers):
    for answer in answers:
        x, y, a = answer
        # 기둥
        if a == 0:
            if y == 0 or ([x - 1, y, 1] in answers or [x, y, 1] in answers or [x, y - 1, 0] in answers):
                continue
            else:
                return False
        # 보
        elif a == 1:
            if [x, y - 1, 0] in answers or [x + 1, y - 1, 0] in answers or ([x - 1, y, 1] in answers and [x + 1, y, 1] in answers):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for b_f in build_frame:
        x, y, a, b = b_f

        # 삭제
        if b == 0:
            answer.remove([x, y, a])
            if check_build(answer) == False:
                answer.append([x, y, a])
        # 설치
        elif b == 1:
            answer.append([x, y, a])
            if check_build(answer) == False:
                answer.remove([x, y, a])
    answer.sort()
    return answer

print(solution(5, 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))