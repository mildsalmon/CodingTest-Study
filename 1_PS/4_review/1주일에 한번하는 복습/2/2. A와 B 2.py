import sys

def dfs(T, S):
    if len(T) == len(S):
        if T == S:
            print(1)
            sys.exit(0)
        return


    if T[0] == 'B':
        temp = T[::-1][:-1]
        dfs(temp, S)

    if T[-1] == 'A':
        temp = T[:-1]
        dfs(temp, S)


if __name__ == "__main__":
    S = input()
    T = input()

    dfs(T, S)

    print(0)