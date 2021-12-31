"""
Date    : 2021.12.31
Update  : 2021.12.31
Source  : 타겟 넘버.py
Purpose : DFS
url     : https://programmers.co.kr/learn/courses/30/lessons/43165
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(depth: int, numbers: list, target: int) -> None:
    global count

    # 종료조건
    # 합이 target과 같거나 작으면 더 이상 재귀를 수행할 필요가 없으므로 재귀 종료
    if sum(numbers) < target:
        return
    elif sum(numbers) == target:
        count += 1
        print(depth, numbers)
        return

    # 수평 탐색
    # 재귀가 아래로 내려가는 거라면, 재귀 안에서는 다음 노드를 수평적으로 탐색함.
    for i in range(depth, len(numbers)):
        numbers[i] = -numbers[i]
        dfs(i + 1, numbers, target)
        numbers[i] = -numbers[i]
    return


def solution(numbers: list, target: int) -> int:
    global count

    count: int = 0
    dfs(0, numbers, target)

    return count

if __name__ == "__main__":
    print(solution([1,1,2,2,1], 3))
