# def d(set_n, n):
#     s_n = str(n)
#     result = n
#     print("s_n", s_n)
#     for i in s_n:
#         result += int(i)
#
#     set_n.add(result)
#     if n > 10000:
#         return
#     d(set_n, n+1)
#
#
# set_n = set()
# d(set_n, 1)

def d(n):
    s_n = str(n)
    result = n

    for i in s_n:
        result += int(i)

    return result

set_n = set()
list_n = [i for i in range(1, 10001)]

for i in range(10001):
    set_n.add(d(i))

# set_n = list(set_n)

for i in list_n:
    if i not in set_n:
        print(i)


# print(set_n)