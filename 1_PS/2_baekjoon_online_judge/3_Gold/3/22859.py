"""
Date    : 2022.02.12
Update  : 2022.02.12
Source  : 22859.py
Purpose : 문자열 / 구현 / 정규식
url     : https://www.acmicpc.net/problem/22859
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

def div(html: str) -> None:
    """
    div 태그가 닫는 태그가 아니라면 title을 출력.
    """
    if "/div" not in html.replace(' ', ''):
        # title의 형태가 title="A"라서 왼쪽에서 count하는 index와 오른쪽에서 count하는 index를 사용하여 슬라이싱함.
        text = "title : " + html[html.index('"')+1:html.rindex('"')]
        print(text)

def p(html: str) -> None:
    """
    p 태그가 존재하는 문장에 여는 괄호와 닫는 괄호를 구함.
    [i번째 닫는 괄호: i+1번째 여는 괄호]로 슬라이싱하면, 태그 사이에 text를 추출할 수 있음
    text가 공백으로만 이루어진 경우를 제외하고 texts 리스트에 추가.
    texts 리스트는 공백이 2번이상인 경우 1개로 변환.
    """
    starts, ends = find_start_end(html)
    texts = []

    for i, value in enumerate(starts[1:]):
        start = value
        end = ends[i]

        # if html[end+1:start].strip():
        texts.append(html[end+1:start])

    text = ''.join(texts).strip()

    while "  " in text:
        text = text.replace("  ", ' ')

    print(text)

def open(html: str) -> None:
    """
    html에서 문단을 나누는 div와 문장을 의미하는 p 태그를 파싱함.
    즉, 현재 태그를 파악하고 원하는 태그만 선별.
    """
    starts, ends = find_start_end(html)

    for i, value in enumerate(starts):
        start = value
        end = ends[i]

        # print(html[start:end+1])

        # '/ div'같은 태그를 제외하기 위해 replace함
        if "div" in html[start:end+1].replace(' ', ''):
            div(html[start:end+1])
        # 'p' 태그 사이에 다양한 태그가 올 수 있어서, 'p'태그의 여는 태그와 닫는 태그는 p_end, p_start에 따로 저장
        if "/p" in html[start:end+1].replace(' ', ''):
            p_end = end
            p(html[p_start:p_end+1])
        elif "p" in html[start:end+1].replace(' ', ''):
            p_start = start



def find_start_end(html: str) -> list:
    """
    문서에 존재하는 모든 여는 괄호(<)와 닫는 괄호(>)의 index를 구함.
    여는 괄호가 존재하면 반드시 닫는 괄호가 존재하기 때문에 starts와 ends의 길이는 동일함.
    """
    starts = []
    ends = []

    for i, value in enumerate(html):
        if value == "<":
            starts.append(i)
        elif value == ">":
            ends.append(i)

    return starts, ends


if __name__ == "__main__":
    html = input()

    # print(html)

    open(html)