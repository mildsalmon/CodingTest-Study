array = list(map(int, input().split()))

scale = [i for i in range(1, 9)]
scale_2 = sorted(scale, reverse=True)
ascending = 0
descending = 0
mixed = 0

for i in range(len(scale)):
    if array[i] == scale[i]:
        ascending += 1
    elif array[i] == scale_2[i]:
        descending += 1
    else:
        mixed += 1

if ascending == 8:
    print("ascending")
elif descending == 8:
    print("descending")
else:
    print("mixed")