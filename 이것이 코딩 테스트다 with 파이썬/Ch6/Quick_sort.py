array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot_data = array[0]
#     tail = array[1:]
#
#     left_list = [x for x in tail if x <= pivot_data]
#     right_list = [x for x in tail if x > pivot_data]
#
#     return quick_sort(left_list) + [pivot_data] + quick_sort(right_list)
#
# quick = quick_sort(array)
#
# print(quick)