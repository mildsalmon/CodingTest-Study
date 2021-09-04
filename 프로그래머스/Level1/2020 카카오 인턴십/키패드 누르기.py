def solution(numbers, hand):
    answer = []
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    hand_pos = [[3, 0], [3, 2]]
    key_pad = [[3, 1],
               [0, 0], [0, 1], [0, 2],
               [1, 0], [1, 1], [1, 2],
               [2, 0], [2, 1], [2, 2]]
    hand_dict = {'left': 0,
                 'right': 1}
    hand_num = hand_dict[hand]

    for number in numbers:
        if number in [1, 4, 7]:
            answer.append("L")
            hand_pos[0] = key_pad[number]
        elif number in [3, 6, 9]:
            answer.append("R")
            hand_pos[1] = key_pad[number]
        elif number in [2, 5, 8, 0]:
            L_diff_x = key_pad[number][0] - hand_pos[0][0]
            L_diff_y = key_pad[number][1] - hand_pos[0][1]
            R_diff_x = key_pad[number][0] - hand_pos[1][0]
            R_diff_y = hand_pos[1][1] - key_pad[number][1]

            if L_diff_x < 0:
                L_diff_x = L_diff_x * -1
            if R_diff_x < 0:
                R_diff_x = R_diff_x * -1

            a = L_diff_y + L_diff_x
            b = R_diff_y + R_diff_x

            if a > b:
                answer.append("R")
                hand_pos[1] = key_pad[number]
            elif a < b:
                answer.append("L")
                hand_pos[0] = key_pad[number]
            elif a == b:
                if hand_num == 0:
                    answer.append("L")
                elif hand_num == 1:
                    answer.append("R")
                hand_pos[hand_num] = key_pad[number]
    answer = ''.join(answer)

    return answer