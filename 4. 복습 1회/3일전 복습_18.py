# # Ch10_그래프_커리큘럼
#
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]    # 각 노드 다음에 어떤 노드로 갈지 들어 있는 그래프
                                    # 즉, 다음 강의 번호가 들어 있음
time = [0] * (n+1)  # 각 강의별 강의시간
# time = [[] for _ in range(n+1)] # 이 방법은 2차원 리스트를 만듬 / 그래서 이 문제에서는 적절하지 않음
indegree = [0] * (n+1)  # 진입 차수 /  각 강의별 몇 개의 강의가 클리어 되었는지 확인

for i in range(1, n+1):
    array = list(map(int, input().split())) # time, (선행 강의(개수 미정)), -1 (마침)
    time[i] = array[0]  # 강의시간은 따로 보관

    for j in array[1:-1]:   # 선행 강의
        graph[j].append(i)  # 그래프에는 선행 강의는 다음 강의가 어디인지 가리켜야함.
                            # input은 현재 노드(i)를 수강하기 위해 선행 강의(j)가 무엇인지 주고 있음.
        indegree[i] += 1    # 현재 노드(i)에 선행 강의 수만큼 진입 차수를 증가

q = deque()
result_time = time[:]   # 누적 강의시간 => 현재 강의를 포함하여 과거 강의시간들의 최댓값

for i in range(1, n+1):
    if indegree[i] == 0:    # 시작 강의를 선택해야함.
        q.append(i)         # 진입 차수가 0인 것이 선행 강의가 없는 것이므로 선택.

while q:
    node = q.popleft()

    for i in graph[node]:   # 여기서 node는 현재 수강하는 강의, i는 다음 강의
        result_time[i] = max(result_time[i], result_time[node] + time[i]) # 다음 강의의 누적 강의시간은
                # (기존 누적 강의시간)과 (현재 수강하는 강의(node)의 누적 강의시간과 다음 강의(i)의 수강시간의 합)
                # 중 최댓값을 선정
        indegree[i] -= 1    # 현재 강의(node)에 대한 처리가 끝났기 때문에, 다음 강의(i)의 진입 차수를 하나 빼줌

        if indegree[i] == 0:    # 새롭게 진입 차수가 0인 강의를 q에 집어넣음.
            q.append(i)

print(*result_time[1:], sep='\n')

# 24분 20초 / pass

# Ch11_그리디_모험가 길드

n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)    # 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
                            # 따라서, 공포도가 큰 모험가부터 그룹을 만듬.
number = 0     # 공포도 + 현재 인덱스 => 그룹 시작 위치(인덱스)
len_array = len(array)  # 모험가의 수
count = 0   # 성공적으로 만들어진 그룹의 수

group = []  # 문제에 나와있지는 않지만, 모험가 그룹을 시각화하여 표현

for i in range(len(array)):
    if i == number:     # 현재 인덱스와 그룹 시작 위치가 같다면
        number += array[i]  # 현재 인덱스(공포도)를 그룹 시작 위치에 더한다. / 공포도가 숫자이고 공포도만큼 그룹지어야하기 때문에 가능한 코드
        if number <= len_array: # 그룹 시작 위치가 전체 모험가의 수를 벗어나지 않으면 if문 진입
            count += 1
            group.append(array[i:number])

print(count)
print(group)

# 12분 / pass


# 반례

# 5
# 1 1 1 1 1
#
# 5
# 4 4 4 4 4
#
# 5
# 1 2 4 3 1
#
# 5
# 2 3 1 2 2