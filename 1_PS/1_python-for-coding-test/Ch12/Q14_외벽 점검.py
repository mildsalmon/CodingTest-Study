from itertools import permutations


def solution(n, weak, dist):
    weak_len = len(weak)
    answer = len(dist) + 1
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for start in range(weak_len):

        for friend in list(permutations(dist, len(dist))):
            count = 1
            pos = weak[start] + friend[count - 1]
            for i in range(start, start + weak_len):
                if pos < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    pos = weak[i] + friend[count-1 ]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])