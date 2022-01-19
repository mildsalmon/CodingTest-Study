"""
Date    : 2022.01.03
Update  : 2022.01.03
Source  : 15683.py
Purpose : 구현 문제 / dfs
url     : https://www.acmicpc.net/problem/15683
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dfs(x, y, visited, walls, d) -> None:
    """
    현재 위치에서 cctv가 감시할 수 있는 맵의 끝까지 직진하기 위한 함수
    """
    global n, m

    # 맵을 벗어나는지 체크
    if 0 <= x < n and 0 <= y < m:
        # 벽을 만났는지 체크
        if (x, y) not in walls:
            visited[x][y] = True

            dx = x + Global.ds[d][0]
            dy = y + Global.ds[d][1]

            dfs(dx, dy, visited, walls, d)

    return

def check_blind_spot(visited) -> int:
    """
    사각지대 크기를 탐색함.
    :param visited: cctv가 감시중인 영역들
    :return: 사각지대 크기
    """
    count: int = 0

    for v in visited:
        count += v.count(False)

    return count

def cctv_move(cctvs, walls, visited, depth) -> None:
    """
    cctv들을 순차적으로 탐색하며 사각지대의 최소 크기를 찾음.
    """
    global n, m, answer

    # 종료조건
    if depth == len(cctvs):
        answer = min(answer, check_blind_spot(visited))

        return

    # 완전 탐색
    cctv, x, y = cctvs[depth]
    # 현재 cctv가 볼 수 있는 방향들
    now_cctv_paths: list[list] = Global.cctv_path[cctv]

    # now_cctv_path는 한번에 볼 수 있는 방향
    for now_cctv_path in now_cctv_paths:
        # copy를 사용하지 않고 visited를 복제함.
        temp_visited: list = [i[:] for i in visited]

        # cctv는 벽을 만나기 전까지 현재 방향에서 직선거리에 있는 방향을 전부 감시한다.
        # 한번에 볼 수 있는 방향을 최대 4방향(동,서,남,북)으로 분리해서 직선거리를 체크해야함.
        # one_path는 현재 보고있는 방향
        for one_path in now_cctv_path:
            dx: int = x + Global.ds[one_path][0]
            dy: int = y + Global.ds[one_path][1]

            # dfs에서 현재 방향이 유효한지는 검사해주지만, 불필요한 연산을 줄이기 위해 여기서도 유효한 방향인지 체크함.
            if 0 <= dx < n and 0 <= dy < m:
                # 직선거리 체크
                dfs(dx, dy, temp_visited, walls, one_path)
        # 다음 cctv로 진입
        cctv_move(cctvs, walls, temp_visited, depth+1)

    # print(*temp_visited, sep='\n')

class Global:
    # static 변수
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

    # list[list]는 cctv가 한번에 볼 수 있는 방향
    # 4번 cctv는 총 4방향을 볼 수 있는데, 한번에 [0, 1, 2], [1, 2, 3] ... 만 볼 수 있음
    cctv_path = {1: [[0], [1], [2], [3]],
                 2: [[0, 2], [1, 3]],
                 3: [[0, 1], [1, 2], [2, 3], [3, 0]],
                 4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
                 5: [[0, 1, 2, 3]]}
    ##########

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    # visited를 사용하지 않았다면, graph를 사용했을텐데, 이 코드에서는 쓸모 없는 변수
    graph: list = []
    cctvs: list = []
    # walls은 dfs함수에서 단순 체크용도이기 떄문에 set으로 설정하여 탐색 시간을 절약.
    walls: set = set()

    visited: list = [[False] * m for _ in range(n)]
    # 구하는 값이 사각지대의 최소 크기이기 때문에 상반되는 최대값을 넣음.
    answer: int = 1e9

    for i in range(n):
        temp: list = list(map(int, input().split()))

        graph.append(temp)

        for j in range(m):
            if temp[j] != 0:
                if 1 <= temp[j] <= 5:
                    # cctv마다 감시 영역이 다르기 때문에 (cctv 번호, x, y)를 cctvs에 넣음
                    cctvs.append((temp[j], i, j))
                elif temp[j] == 6:
                    walls.add((i, j))
                # cctv위치, 벽 위치는 사각 지대에 포함되지 않기 때문에 방문 체크함.
                visited[i][j] = True

    # 가장 많은 범위를 감시하는 cctv부터 처리하기 위해 DESC 정렬함.
    cctvs.sort(key=lambda x: -x[0])

    cctv_move(cctvs, walls, visited, 0)

    print(answer)