import math


def solution(w, h):
    gcd = math.gcd(w, h)

    if gcd == 1:
        answer = w + h - 1
    elif gcd > 1:
        answer = gcd * ((w // gcd) + (h // gcd) - 1)

    return w * h - answer