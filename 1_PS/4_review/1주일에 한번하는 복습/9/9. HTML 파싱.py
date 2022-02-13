"""
Date    : 2022.02.13
Update  : 2022.02.13
Source  : 22859.py
Purpose : 구현 / 문자열 / 파싱
url     : https://www.acmicpc.net/problem/22859
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

import re

if __name__ == "__main__":
    html = input()

    html = html[len('<main>'):-len('</main>')]
    html = re.sub(r'<div title="([\w ]*)">', r'title : \1\n', html)
    html = re.sub(r'</div>', '', html)
    html = re.sub(r'<p>', '', html)
    html = re.sub(r'</p>', '\n', html)
    html = re.sub(r'</?[\w ]*>', '', html)
    html = re.sub(r' *\n *', '\n', html)
    html = re.sub(r' {2,}', ' ', html)

    print(html)
