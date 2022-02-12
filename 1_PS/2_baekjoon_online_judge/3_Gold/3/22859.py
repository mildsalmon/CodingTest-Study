"""
Date    : 2022.02.12
Update  : 2022.02.12
Source  : 22859.py
Purpose : 문자열 / 구현 / 정규식
url     : https://www.acmicpc.net/problem/22859
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def prettify(s):
    detag = ''
    tagged = False
    for c in s:
        if c == '<': tagged = True
        elif c == '>': tagged = False
        elif not tagged: detag+= c
    return ' '.join(detag.split())

if __name__ == '__main__':
    S = input()
    S = S[6:-13]
    S = S.split("</div>")
    for para in S:
        sents = para.split("<p>")
        title = sents[0][12:-2]
        print(f"title : {title}")
        for sent in sents[1:]:
            print(prettify(sent[:-4]))