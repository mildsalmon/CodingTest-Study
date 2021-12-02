"""
Date    : 2021.12.02
Update  : 2021.12.03
Source  : 1283.py
Purpose : 단축키 지정 - 문자열을 이용한 구현문제.
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

n = int(input())

# 단축키로 지정될 단어의 알파벳 대문자 저장
keys = []
# 출력에서 원하는 방식으로 변경한 문자열 저장
answer = []

for i in range(n):
    # 나중에 이 문자열만 사용해야해서, 문자열(옵션)을 있는 그대로 받았다.
    temp = input()
    # 문자열에서 공백(띄어쓰기)를 기준으로 split했다.
    temp_split = temp.split()

    # 최종 문자열(옵션)을 저장함. -> New => [N]ew
    word_concat = ''
    # 현재 옵션에 대해 단어의 첫 글자가 단축키로 지정되어 있지 않으면 True로 변경하고 단축키를 지정한다.
    set_word = False

    # 옵션을 단어별로 구분해서 첫 글자가 단축키로 지정되어 있는지 확인해야한다.
    # 그래서 split된 문자열을 사용한다.
    for t in temp_split:
        # 알파벳의 대소문자를 구분하지 않는다고 했다.
        # 그래서 모든 알파벳은 대문자로 치환하여 비교하였다.
        # 단어의 첫 글자의 대문자가 keys(단축키 저장 리스트)에 없고 set_word(단축키 지정 여부)가 False라면 단축키를 지정한다.
        if t[0].upper() not in keys and set_word == False:
            # keys에 저장되는 알파벳도 전부 대문자이다.
            keys.append(t[0].upper())
            # 지정한 단축키 앞, 뒤에 괄호([ ])를 삽입하고 최종 문자열에 더한다(concat).
            word_concat += "[" + t[0] + "]" + t[1:]
            # 이 옵션에서 단축키를 지정했기 때문에 set_word를 True로 변경한다.
            set_word = True
        else:
            # 단어의 첫 글자의 대문자가 keys에 저장되어 있거나 이미 이 옵션에서 단축키를 지정했다면(set_word == True)
            # 그냥 word_concat에 현재 단어를 더한다(concat).
            word_concat += t
        # 옵션의 단어 사이에는 띄어쓰기가 있기 때문에 for문의 마지막 위치에 띄어쓰기를 추가한다.
        word_concat += " "

    # 첫 글자의 대문자가 keys에 저장되어 있고, 단축키가 지정되지 않은 옵션은 아래 조건문에 들어간다.
    if not set_word:
        # range로 index를 처리하기 번거로울거 같아서 enumerate를 사용했다.
        # 여기서는 split하지 않은 문자열을 사용한다.
        # 옵션을 단어별로 첫 글자가 keys에 저장되지 않은 값을 찾는것이 아닌,
        #   단축키로 지정되지 않은 문자 중 가장 앞에 있는 문자를 선택해서 단축키로 지정해야 하기 때문.
        for j, t in enumerate(temp):
            # 문자의 대문자가 keys에 없고 문자가 공백이 아니라면 if문을 실행한다.
            if t.upper() not in keys and t != " ":
                # 문자열 인덱싱을 이용하여 출력해야하는 형식으로 변경한다.
                word_concat = temp[:j] + "[" + temp[j] + "]" + temp[j+1:]
                # 여기서 찾은 단축키를 keys에 저장하낟.
                keys.append(t.upper())
                break

    # 문자열 마지막에 공백이 추가되었을 수 있으므로 strip()으로 정리해준다.
    answer.append(word_concat.strip())

print(*answer, sep='\n')
