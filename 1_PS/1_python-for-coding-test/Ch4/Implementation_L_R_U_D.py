n = int(input())
plan_list = list(map(str, input().split()))

position = [1, 1]

for plan in plan_list:
  if plan == "L" and position[1] > 1:
    position[1] = position[1] - 1
  elif plan == "R" and position[1] < n:
    position[1] = position[1] + 1
  elif plan == "U" and position[0] > 1:
    position[0] = position[0] - 1
  elif plan == "D" and position[0] < n:
    position[0] = position[0] + 1

print(position)