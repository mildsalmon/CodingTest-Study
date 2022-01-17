"""
Date    : 2022.01.17
Update  : 2022.01.17
Source  : 4256.py
Purpose :
url     : https://www.acmicpc.net/problem/4256
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import sys

input = sys.stdin.readline


if __name__ == "__main__":
    for tc in range(int(input())):
        node_num = int(input())
        # preorder는 root - left - right
        pre_order = list(map(int, input().split()))
        # inorder는 left - root - right
        in_order = list(map(int, input().split()))
        # postorder는 left - right - root
        post_order = []
