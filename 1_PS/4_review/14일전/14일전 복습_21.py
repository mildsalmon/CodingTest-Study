# 무지의 먹방 라이브

def solution(food_times, k):
    foods = [[food_times[i], i + 1] for i in range(len(food_times))]

    foods.sort()
    pre_food = 0
    food_len = len(food_times)

    for i in range(food_len):
        now_food = foods[i][0]
        diff = now_food - pre_food

        if diff > 0:
            spend = diff * food_len
            if spend > k:
                k = k % food_len
                temp = foods[i:]
                temp.sort(key=lambda x: x[1])
                return temp[k][1]
            else:
                k -= spend
                pre_food = now_food
        else:
            pass
        food_len -= 1

    return -1