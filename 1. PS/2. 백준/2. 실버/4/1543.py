"""
Date    : 2021.12.06
Update  : 2021.12.06
Source  : 1543.py
Purpose : 문자열 다루기
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
# 기능별로 함수를 나눠서 구현.
def doc_search(step):
    count = 0

    while step < len(doc):
        # 찾고자하는 단어가 있다면, 단어 길이만큼 step을 증가시킴
        if doc[step:step + len(word)] == word:
            step += len(word)
            count += 1
        # 없다면, 다음 문자부터 단어 길이만큼 비교
        else:
            step += 1

    print(count)


if __name__ == "__main__":
    doc = input()
    word = input()

    count = doc_search(0)