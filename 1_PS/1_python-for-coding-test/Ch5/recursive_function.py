def recursive_function():
    print("재귀 함수 호출")
    recursive_function()

# recursive_function()

def recursive_function_2(i):
    if i == 10:
        return
    else:
        print("{0} 번째 재귀 함수에서 {1} 번째 재귀 함수를 호출합니다.".format(i, i+1))
        recursive_function_2(i+1)
        print("{0} 번째 재귀 함수를 종료합니다.".format(i))

# recursive_function_2(1)

def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적으로 구현 : {0}".format(factorial_iterative(5)))
print("재귀적으로 구현 : {0}".format(factorial_recursive(5)))