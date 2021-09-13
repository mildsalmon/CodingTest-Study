n = list(map(int, input()))

len_n = len(n)
half_n = len_n // 2
left_sum = sum(n[:half_n])
right_sum = sum(n[half_n:])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

# 5분 40초 / pass