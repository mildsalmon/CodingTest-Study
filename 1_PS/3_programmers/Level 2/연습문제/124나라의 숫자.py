def solution(n):
    a = []
    n = int(n)
    while n != 0:
        if n % 3 == 0:
            a.append(str(4))
            n = n // 3
            n -= 1
        else:
            a.append(str(n%3))
            n = n // 3
    a.reverse()
    answer = ''.join(a)
    return answer