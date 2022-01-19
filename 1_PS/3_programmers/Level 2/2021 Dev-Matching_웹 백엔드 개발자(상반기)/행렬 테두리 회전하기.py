def solution(rows, columns, queries):
    array = []

    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(i * columns + (j + 1))
        array.append(temp)

    answer = []

    for i in queries:
        x_1, y_1, x_2, y_2 = i
        row_len = x_2 - x_1
        column_len = y_2 - y_1
        dx, dy = x_1 - 1, y_1 - 1

        temp = [array[dx][dy]]
        # temp = []

        for j in range(column_len):
            dy += 1
            temp.append(array[dx][dy])
            array[dx][dy] = temp[-2]

        for j in range(row_len):
            dx += 1
            temp.append(array[dx][dy])
            array[dx][dy] = temp[-2]

        for j in range(column_len):
            dy -= 1
            temp.append(array[dx][dy])
            array[dx][dy] = temp[-2]

        for j in range(row_len):
            dx -= 1
            temp.append(array[dx][dy])
            array[dx][dy] = temp[-2]

        # print(temp)
        answer.append(min(temp))

    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])