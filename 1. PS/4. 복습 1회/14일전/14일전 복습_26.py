# 기둥과 보

def check(answers):
    for answer in answers:
        x, y, a = answer

        # 기둥
        if a == 0:
            if y == 0 or (x - 1, y, 1) in answers or (x, y, 1) in answers or (x, y - 1, 0) in answers:
                continue
            else:
                return False
        # 보
        elif a == 1:
            if (x, y - 1, 0) in answers or (x + 1, y - 1, 0) in answers or (
                    (x - 1, y, 1) in answers and (x + 1, y, 1) in answers):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for build in build_frame:
        x, y, a, b = build

        # 삭제
        if b == 0:
            answer.remove((x, y, a))
            if not check(answer):
                answer.append((x, y, a))

        # 설치
        elif b == 1:
            answer.append((x, y, a))
            if not check(answer):
                answer.remove((x, y, a))

    answer.sort()

    return answer