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

def search_root_node(pre_order: list) -> int:
    """
    root node 추출
    """
    return pre_order.pop(0)

def search_post_order(pre_order: list, in_order: list, post_order: list) -> None:
    """
    1. root node부터 찾는다.
        - root node는 preorder를 통해 찾을 수 있다.
        - preorder는 (tree의 root node - left sub tree의 root node - right sub tree의 root node)를 가지고 있다.
    2. root node를 기준으로 inorder를 통해 left / right sub tree를 분리한다.
    3. sub tree의 원소가 0이 될때까지 sub tree를 찾는다. (재귀)
    4. left / right sub tree가 없을 경우(자식 node가 없는 경우) root node를 postorder에 추가한다.

    ===
    preorder : 3 6 5 4 8 7 1 2
    inorder  : 5 6 8 4 3 1 2 7

    현재 sub tree의 root node = 3
    left sub tree            = 5 6 8 4
    rifgt sub tree           = 1 2 7

    이걸 반복
    """
    root_node = search_root_node(pre_order)
    left_sub_tree = in_order[:in_order.index(root_node)]
    if len(left_sub_tree) >= 1:
        search_post_order(pre_order, left_sub_tree, post_order)
    right_sub_tree = in_order[in_order.index(root_node)+1:]
    if len(right_sub_tree) >= 1:
        search_post_order(pre_order, right_sub_tree, post_order)

    post_order.append(root_node)

if __name__ == "__main__":
    for tc in range(int(input())):
        node_num = int(input())
        # preorder는 root - left - right
        pre_order = list(map(int, input().split()))
        # inorder는 left - root - right
        in_order = list(map(int, input().split()))
        # postorder는 left - right - root
        post_order = []

        search_post_order(pre_order, in_order, post_order)

        print(*map(str, post_order))