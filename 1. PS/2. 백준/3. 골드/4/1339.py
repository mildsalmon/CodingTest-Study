"""
Date    : 2021.12.15
Update  : 2021.12.15
Source  : 단어 수학.py
Purpose : 문자열 문제인줄 알았으나, 수학 문제였음..
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""

n = int(input())

arrays = []
max_len = 0

for _ in range(n):
    temp = input()
    arrays.append(temp)
    max_len = max(max_len, len(temp))

# 초기에 리스트의 원소 10개를 사용하지 않는 문자 'Z'로 초기화
checked = ['Z'] * 10

"""
문자열이 "GCF", "ACDEB"라면 

  GCF
ACDEB

이런 구조로 만들어서, 왼쪽 문자부터 checked 리스트에 (오른쪽 인덱스 -> 왼쪽 인덱스) 순서로 집어넣는다.

A = checked[9]
C = checked[8]
G = checked[7]
D = checked[6]
C = x (이미 checked 리스트에 존재하여 패스)
E = checked[5]
F = checked[4]
B = checked[3]
"""
for i in range(max_len):
    for array in arrays:
        if len(array) >= max_len - i:
            index = len(array) - max_len + i
            for j in range(9, -1, -1):
                if array[index] not in checked:
                    if checked[j] == 'Z':
                        checked[j] = array[index]
                        # print(checked)
                        break
                else:
                    break

new_arrays = []

"""
문자열을 "GCF", "ACDEB" -> 784, 98653로 치환해야함.

checked = ['Z', 'Z', 'Z', 'B', 'F', 'E', 'D', 'G', 'C', 'A']

문자열을 문자 단위로 쪼개서 chekced 리스트의 인덱스 번호를 가져옴.
그리고 문자열로 변환하여 concat을 함
"""
for array in arrays:
    new_string = ''
    for string in array:
        new_string += str(checked.index(string))
    new_arrays.append(new_string)

answer = 0

"""
원하는 결과는 주어진 단어의 합의 최댓값이라서 각 원소를 int로 변환하고 합함.
"""
for num in new_arrays:
    answer += int(num)

print(answer)

"""
완벽하게 풀었다고 생각하였으나, 이런 방식으로 푸는 문제가 아니었음.

# 반례

10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB

정답값 : 1790
출력값 : 1780
"""

"""
이 문제는 문자열(알파벳)의 위치에 따라 숫자로 변환하는 것이 아니라,
문자열의 발생 횟수를 계산하여, 가장 많이 발생한 순서부터 9~0 순서로 곱하는 문제였음... 
"""