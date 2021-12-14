"""
Date    : 2021.12.09
Update  : 2021.12.13
Source  : Q46_아기 상어.py
Purpose : dfs로 구현한 것을 클래스로 변경함.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
def rank():
    answer = 0

    for i in range(1, len(counting_sort)):
        if counting_sort[i] != 1:
            if counting_sort[i] >= 2:
                # 현재 순위 * 순위변경이 필요한 인원 수
                answer += i * (counting_sort[i] - 1)
            elif counting_sort[i] == 0:
                answer -= i

    if answer < 0:
        return -answer
    elif answer >= 0:
        return answer

if __name__ == "__main__":
    n = int(input())
    counting_sort = [0] * (n+1)

    for _ in range(n):
        temp = int(input())
        counting_sort[temp] += 1

    print(rank())