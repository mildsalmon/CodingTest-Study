"""
Date    : 2022.04.10
Update  : 2022.04.10
Source  : [1차] 다트 게임.py
Purpose : re / 정규식 / dict - lambda
url     : https://programmers.co.kr/learn/courses/30/lessons/17682
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import re


def solution(dartResult):
    answer = []
    oper = {'S': lambda x: x,
            'D': lambda x: x ** 2,
            'T': lambda x: x ** 3}

    com = re.compile(r'\d+[SDT]+[#*]*')
    dart = re.findall(com, dartResult)

    for d in dart:
        score = int(re.findall(r'\d+', d)[0])
        bonus = re.findall(r'[SDT]+', d)[0]
        option = re.findall(r'[#*]+', d)

        score = oper[bonus](score)

        if option:
            if option[0] == '*':
                if answer:
                    answer[-1] *= 2
                score *= 2
            elif option[0] == '#':
                score *= -1

        answer.append(score)

    return sum(answer)