# Ch11_그리디_무지의 먹방 라이브

def solution(food_times, k):
    foods = [[food_times[i], i + 1] for i in range(len(food_times))]

    foods.sort()

    food_len = len(food_times)
    pre_food_time = 0

    for i, food in enumerate(foods):
        now_food_time = food[0]
        diff = now_food_time - pre_food_time

        if diff > 0:
            spend = diff * food_len
            if spend <= k:
                k -= spend
                pre_food_time = now_food_time
            elif spend > k:
                k %= food_len
                answer = sorted(foods[i:], key=lambda x: x[1])
                # print(spend, k)
                return answer[k][1]

        food_len -= 1

    return -1

# 22분