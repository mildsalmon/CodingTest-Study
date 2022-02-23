"""
Date    : 2022.02.23
Update  : 2022.02.23
Source  : 13022.py
Purpose :
url     : https://www.acmicpc.net/problem/13022
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""


def check(seq, dic):
    if ''.join(seq) == 'wolf' and dic['w'] == dic['o'] == dic['l'] == dic['f']:
        seq.clear()

        for key, value in dic.items():
           dic[key] = 0
    else:
        return False
    return True


def solution(word):
    if len(word) < 4:
        return 0

    # wolf 순서 체크를 위한 seq
    former = word[0]
    seq = [former]

    # wolf 개수 체크를 위한 dic
    dic = dict(w=0, o=0, l=0, f=0)
    dic[former] = 1
    flag = True

    for i in range(1, len(word)):
        if word[i] != former:
            if former == 'f':
                flag = check(seq, dic)
            seq.append(word[i])
            former = word[i]

        dic[word[i]] += 1

        if i == len(word) - 1:
            flag = check(seq, dic)

        if not flag:
            return 0

    return 1


if __name__ == "__main__":
    print(solution(input()))

    # print(solution('wolwolff'))
    # print(solution('wolf'))
    # print(solution('wwolfolf'))
    # print(solution('wwwoolllfff'))
    # print(solution('wwolfolf'))
    # print(solution('wfol'))
    # print(solution('wolfwwoollffwolf'))
    # print(solution('wolf'))
    # print(solution('wwoollff'))
    # print(solution('wwwooolllfff'))
    # '''
    # 0
    # 1
    # 0
    # 0
    # 0
    # 0
    # 0
    # 1
    # 1
    # 1
    # 1
    # '''