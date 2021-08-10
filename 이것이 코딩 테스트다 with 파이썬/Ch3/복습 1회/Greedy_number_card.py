n, m = list(map(int, input().split()))

# min_cards = []
max_card = 0

for i in range(n):
    card_numbers = list(map(int, input().split()))
    min_card = min(card_numbers)
    max_card = max(min_card, max_card)

    # min_cards.append(min_card)

print(max_card)