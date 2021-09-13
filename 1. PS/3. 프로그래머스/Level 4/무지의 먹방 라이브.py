def solution(food_times, k):
    foods = [[food_times[i], i + 1] for i in range(len(food_times))]

    foods.sort()

    pre_time = 0
    len_foods = len(foods)

    for i in range(len(foods)):
        now_time = foods[i][0]
        h = now_time - pre_time

        if h > 0:
            eat = h * len_foods

            if eat <= k:
                k -= eat
                pre_time = now_time
            elif eat > k:
                k %= len_foods
                food_resort = sorted(foods[i:], key=lambda x: x[1])
                return food_resort[k][1]
        len_foods -= 1

    return -1
if __name__ == "__main__":
    solution([3, 1, 2], 5)
