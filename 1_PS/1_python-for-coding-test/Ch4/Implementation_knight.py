n = input()

x_full = {'a': 1,
          'b': 2,
          'c': 3,
          'd': 4,
          'e': 5,
          'f': 6,
          'g': 7,
          'h': 8}
# y_limit = '8'

x = x_full[n[0]]
y = n[1]

count = 0

# count = count + 1

# one_commend = [1, 1, ]
# two_commend = []

# if x + 2 < 9 or x - 2 > 0:
#   if y + 1 < 9 or y - 1 > 9:
    
commands = [['l','l','u'],
          ['l','l','d'],
          ['r','r','u'],
          ['r','r','d'],
          ['u','u','l'],
          ['u','u','r'],
          ['d','d','l'],
          ['d','d','r']]

for command in commands:
  x_copy = int(x)
  y_copy = int(y)

  for move in command:
    if move == 'l':
      x_copy = x_copy - 1
    elif move == 'r':
      x_copy = x_copy + 1
    elif move == 'u':
      y_copy = y_copy + 1
    elif move == 'd':
      y_copy = y_copy - 1
  
  if x_copy > 0 and x_copy < 9 and y_copy > 0 and y_copy < 9:
    count = count + 1
    
print(count)
