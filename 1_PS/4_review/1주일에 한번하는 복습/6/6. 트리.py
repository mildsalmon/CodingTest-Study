"""
Date    : 2022.01.22
Update  : 2022.01.22
Source  : 4256.py
Purpose : 트리 / 분할 정복 / 재귀
url     : https://www.acmicpc.net/problem/4256
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def make_postorder(preorder: list, inorder: list, postorder: list) -> None:
    global n

    root_node = preorder.pop()
    left_sub_tree = inorder[:inorder.index(root_node)]
    right_sub_tree = inorder[inorder.index(root_node)+1:]

    if left_sub_tree:
        make_postorder(preorder, left_sub_tree, postorder)
    if right_sub_tree:
        make_postorder(preorder, right_sub_tree, postorder)

    postorder.append(root_node)

if __name__ == "__main__":
    for tc in range(int(input())):
        n = int(input())
        preorder = list(input().split())
        inorder = list(input().split())
        postorder = []

        make_postorder(preorder[::-1], inorder, postorder)

        print(' '.join(postorder))