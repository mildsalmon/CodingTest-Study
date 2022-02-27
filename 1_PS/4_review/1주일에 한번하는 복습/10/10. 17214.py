"""
Date    : 2022.02.27
Update  : 2022.02.27
Source  : 10. 17214.py
Purpose : 정규식 / 문자열
url     : https://www.acmicpc.net/problem/17214
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import re

# def solution(s):
if __name__ == "__main__":
    s = input()

    nums = re.sub(r'x+[+-]', r' ', s).split()
    oper = re.sub(r'[+-]*[\dx]+([+-]+)\d+', r'\1', s)


    if len(nums) == 1:
        if nums[0][-1] == 'x':
            nums[0] = str(int(nums[0][:-1]) // 2)

            if nums[0] == '1':
                print('xx+W')
            elif nums[0] == '-1':
                print('-xx+W')
            else:
                print(nums[0] + 'xx+W')
        else:
            if nums[0] == '1':
                print('x+W')
            elif nums[0] == '-1':
                print('-x+W')
            elif nums[0] == '0':
                print('W')
            else:
                print(nums[0] + 'x+W')
    elif len(nums) == 2:
        nums[0] = str(int(nums[0]) // 2)

        if nums[0] == '1':
            print('xx', end='')
        elif nums[0] == '-1':
            print('-xx', end='')
        else:
            print(nums[0] + 'xx', end='')

        print(oper, end='')

        if nums[1] == '1':
            print('x+W')
        else:
            print(nums[1] + 'x+W')
#
# solution('-1')
# solution('-2x-10')
# solution('-2x')
# solution('-2x-1')
# solution('2x+1')
# solution('6x+6')

