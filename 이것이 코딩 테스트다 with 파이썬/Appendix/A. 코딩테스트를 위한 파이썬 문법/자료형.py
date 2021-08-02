# a = 10
# print(a)
#
# b = -10
# print(b)
#
# c = 0
# print(c)

# a = 123.45
# print(a)
#
# b = -123.45
# print(b)
#
# c = 123.
# print(c)
#
# d = .45
# print(d)

# a = 1e9
# print(a)
#
# b = 123.45e1
# print(b)
#
# c = 123e-3
# print(c)

# a = 0.3 + 0.6
# print(a)
#
# if a == 0.9:
#     print(True)
# else:
#     print(False)

# a = 0.3 + 0.6
# print(round(a, 4))
#
# if round(a, 4) == 0.9:
#     print(True)
# else:
#     print(False)

# a = 7
# b = 3
#
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

# a = [1,2,3,4,5]
# print(a)
#
# print(a[2])
#
# b = list()
# print(b)
#
# c = []
# print(c)

# n = 10
# a = [0] * n
# print(a)

# a = [1,2,3,4,5]
# print(a[-3])
#
# a[1] = 10
# print(a)

# a = [1,2,3,4,5]
#
# print(a[1:3])

# a = [i for i in range(20) if i%2 == 1]
#
# print(a)

# n = 3
# m = 4
# array = [[0] * m for _ in range(n)]
#
# print(array)

# n = 3
# m = 4
# array = [[0] * m] * n
# print(array)
#
# array[1][1] = 5
# print(array)

# a = [1,2,3,4,5,5,5]
# remove_set = [3,5]
#
# result = [i for i in a if i not in remove_set]
# print(result)

# data = 'Hello'
# print(data)
#
# data = "Good \"day\""
# print(data)

# a = "Hello"
# b = "world"
#
# print(a + " " + b)

# a = "A"
# print(a*10)

# a = "asdfgh"
# print(a[1:-3])

# a = (1,2,3,4)
# print(a)
#
# a[2] = 4

# data = dict({'사과': 'apple',
#             '바나나': 'banana'})
# data['코코넛'] = 'coconut'
#
# key_list = data.keys()
# value_list = data.values()
#
# print(key_list)
# print(value_list)
#
# for i in key_list:
#     print(i)

# data = set([1,2,3,4,5,1])
# print(data)
#
# data = {1,2,3,4,5,5}
# print(data)

# a = set([1,2,3,4,5])
# b = set([3,4,5,6,7])
#
# print(a | b)
# print(a & b)
# print(a - b)

data = set([1,2,3])
print(data)

data.add(4)
print(data)

data.update([5,6])
print(data)

data.remove(3)
print(data)