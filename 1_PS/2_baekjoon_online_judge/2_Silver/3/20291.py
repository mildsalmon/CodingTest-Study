"""
Date    : 2021.12.08
Update  : 2021.12.08
Source  : 20291.py
Purpose : key-value 구조인 딕셔너리를 사용하였고, 정렬함수를 사용하여 정렬하였다.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def dict_show_data(file_names) -> None:
    """
    딕셔너리 자료형 매개변수를 출력해줌
    :param file_names:
    :return:
    """
    for key, value in file_names:
        print(key, value)

def solution():
    n = int(input())
    file_names = {}

    for i in range(n):
        name, extension = input().split('.')

        if extension in file_names:
            file_names[extension] += 1
        else:
            file_names[extension] = 1
        # file_names.update({extension:})

    sort_file_names = sorted(file_names.items())

    dict_show_data(sort_file_names)

if __name__ == "__main__":
    solution()