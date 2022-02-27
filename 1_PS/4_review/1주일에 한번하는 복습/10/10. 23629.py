"""
Date    : 2022.02.27
Update  : 2022.02.27
Source  : 10. 23629.py
Purpose : 정규식 / 문자열
url     : https://www.acmicpc.net/problem/23629
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
import re

def str_to_num(s):
    s = re.sub(r'ZERO', r'0', s)
    s = re.sub(r'ONE', r'1', s)
    s = re.sub(r'TWO', r'2', s)
    s = re.sub(r'THREE', r'3', s)
    s = re.sub(r'FOUR', r'4', s)
    s = re.sub(r'FIVE', r'5', s)
    s = re.sub(r'SIX', r'6', s)
    s = re.sub(r'SEVEN', r'7', s)
    s = re.sub(r'EIGHT', r'8', s)
    s = re.sub(r'NINE', r'9', s)

    return s


def check_alpha(text):
    for t in text:
        if t.isalpha() and t != 'x':
            return False
    return True


def extract_oper(s):
    text = re.sub(r'\d', r'', s)
    opers = []

    for oper in text:
        if oper:
            opers.append(oper)

    return opers


def extract_nums(s):
    text = re.sub(r'[-+x/=]', ' ', s)
    text = text.split()
    nums = []

    for num in text:
        if num:
            nums.append(int(num))

    return nums


def calculate(nums, opers):
    result = nums[0]
    opers = opers[:-1]

    for num, oper in zip(nums[1:], opers):
        if oper == '+':
            result += num
        elif oper == '-':
            result -= num
        elif oper == 'x':
            result *= num
        elif oper == '/':
            result /= num
            result = int(result)

    return result


def num_to_str(num):
    num = str(num)

    num = re.sub(r'0', r'ZERO', num)
    num = re.sub(r'1', r'ONE', num)
    num = re.sub(r'2', r'TWO', num)
    num = re.sub(r'3', r'THREE', num)
    num = re.sub(r'4', r'FOUR', num)
    num = re.sub(r'5', r'FIVE', num)
    num = re.sub(r'6', r'SIX', num)
    num = re.sub(r'7', r'SEVEN', num)
    num = re.sub(r'8', r'EIGHT', num)
    num = re.sub(r'9', r'NINE', num)

    return num

if __name__ == "__main__":
    s = input()

    s = str_to_num(s)
    if check_alpha(s):
        opers = extract_oper(s)
        nums = extract_nums(s)

        if len(nums) != len(opers):
            print('Madness!')
        else:
            result = calculate(nums, opers)
            print(s)
            print(num_to_str(result))
    else:
        print("Madness!")
