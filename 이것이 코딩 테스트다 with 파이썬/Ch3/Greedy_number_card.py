n, m = list(map(int, input().split()))
card = list()
choice = list()

for i in range(n):
  card.append(list(map(int, input().split())))
  card[i].sort()
  choice.append(card[i][0])

choice.sort()

print(choice[-1])