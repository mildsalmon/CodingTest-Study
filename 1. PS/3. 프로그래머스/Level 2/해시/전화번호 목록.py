"""
Date    : 2021.12.16
Update  : 2021.12.16
Source  : 전화번호 목록.py
Purpose : 문자열 비교를 통해 해결.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def solution(phone_book):
    """
    sort를 하면 문자열들(['1', '2', '3', '123', '24'])은 ['1', '123', '2', '24', '3'] 으로 정렬된다.
    그럼 현재 인덱스의 문자열과 다음 인덱스의 문자열을 비교하여 접두어인지 확인할 수 있다.
    """
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        phone_len = len(phone_book[i])
        # 다음 인덱스의 문자열의 접두어가 현재 인덱스와 같은지 알기 위해서는
        # 다음 인덱스의 문자열에서 현재 인덱스의 길이만큼만 비교하면 알 수 있다.
        if phone_book[i] == phone_book[i + 1][:phone_len]:
            return False

    return True