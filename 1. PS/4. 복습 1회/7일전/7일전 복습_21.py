# Ch11_그리디_무지의 먹방 라이브

def solution(food_times, k):
    foods = [[food_times[i], i + 1] for i in range(len(food_times))]

    foods.sort()

    len_foods = len(foods)
    pre_food = 0

    for i in range(len_foods):
        now_food = foods[i][0]

        diff_food = now_food - pre_food

        if diff_food != 0:
            eat = diff_food * len_foods

            k = k - eat
            if k >= 0:
                pre_food = now_food
            elif k < 0:
                k %= len_foods

                temp = sorted(foods[i:], key=lambda x: x[1])

                return temp[k][1]

        len_foods -= 1
    return -1

solution([3, 1, 2], 5)

# 29분