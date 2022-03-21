"""
Date    : 2021.12.16
Update  : 2021.03.21
Source  : 전화번호 목록.py
Purpose : 문자열 비교를 통해 해결.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def solution(phone_book):
    phone_book.sort()

    for pre_phone, in_phone in zip(phone_book, phone_book[1:]):
        if in_phone.startswith(pre_phone):
            return False

    return True
