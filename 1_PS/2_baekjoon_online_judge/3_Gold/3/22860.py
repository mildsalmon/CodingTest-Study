"""
Date    : 2022.03.10
Update  : 2022.03.10
Source  : 22860.py
Purpose : dict / dfs / 재귀 / 구현 / 문자열 / 파싱
url     : https://www.acmicpc.net/problem/22860
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import sys

sys.setrecursionlimit(10**5)


def search_file(roots: dict, child: str, files: list):
    for name, flag in roots[child]:
        if flag == '1':
            search_file(roots, name, files)
        else:
            files.append(name)

    return


def counting_file(files: list) -> list:
    file_cnt = len(files)
    file_type_cnt = len(set(files))

    return [file_type_cnt, file_cnt]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    roots = dict()

    for _ in range(n + m):
        P, F, C = input().split()

        if P in roots:
            roots[P].append([F, C])
        else:
            roots[P] = [[F, C]]

        if C == '1' and F not in roots:
            roots[F] = []

    # print(roots)

    q = int(input())

    for _ in range(q):
        temp = input().split('/')
        child = temp[-1]

        # print(child)
        files = []

        search_file(roots, child, files)

        # print(f'file : {files}')
        file_type_cnt, file_cnt = counting_file(files)

        print(file_type_cnt, file_cnt)