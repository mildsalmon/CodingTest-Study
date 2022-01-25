## 🏋️‍♂️ 나만의 시스템

보통 평일과 주말을 나눠서 공부합니다.

평일은 아침 9시 ~ 12시 사이에 한 문제를 풀고 인상깊은 문제는 [블로그](https://blex.me/@mildsalmon/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%97%90-%EB%8C%80%ED%95%B4-%EA%B3%B5%EB%B6%80%ED%95%B4%EB%B3%B4%EC%9E%90)에 해설 포스팅을 남깁니다.

~~주말은 평일에 푼 문제 중 틀린 문제를 복습합니다. (자주 까먹기 때문에 주말에는 문제를 더 풀지 않습니다.)~~  
주말에는 평일에 푼 문제를 복습하고, 새로운 문제들을 풀어봅니다.


## 🖋 지식을 코드에 적용하여 정리해봤어요.

### A. 운영체제

#### a. CPU Scheduling (SJF)

> 현재 시점에서 cpu burst time이 짧은 작업을 우선으로 처리한다.

- 블로그 포스팅

    - [11399번 - ATM (blex.me)](https://blex.me/@mildsalmon/11399%EB%B2%88-atm)
    - [Heap - 디스크 컨트롤러 (blex.me)](https://blex.me/@mildsalmon/heap-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC)

- GitHub Code

    - [Baekjoon - sort - ATM (Github)](https://github.com/mildsalmon/CodingTest-Study/commit/ad8ea9e4cfbecaff44884b85da72221c2acd7b90#diff-f70a24eb102c486bd68b329c4fc0d9c6cdf9e712426fceb10d80ad792c45a0d6)
    - [Programmers - Heap - 디스크 컨트롤러 (Github)](https://github.com/mildsalmon/CodingTest-Study/commits/master/1_PS/3_programmers/Level%203/Heap/%EB%94%94%EC%8A%A4%ED%81%AC%20%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC.py)

### B. 객체지향 프로그래밍

#### a. 아기 상어

> 클래스로 구현하여, 외부에서는 geeter와 setter로만 객체를 제어할 수 있게 하였다. 또한, 메소드별 역할을 적은 주석을 추가하여 가독성을 높였다.

- 블로그 포스팅

    - [16236번 - 아기 상어 (blex.me)](https://blex.me/@mildsalmon/chap-19-%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-q46-%EC%95%84%EA%B8%B0-%EC%83%81%EC%96%B4)

- GitHub Code

    - [Beajoon - 구현 - 아기 상어 (Github)](https://github.com/mildsalmon/CodingTest-Study/commits/master/1.%20PS/1.%20%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4%20with%20%ED%8C%8C%EC%9D%B4%EC%8D%AC/Ch19/Q46_%EC%95%84%EA%B8%B0%20%EC%83%81%EC%96%B4.py)

#### a. 청소년 상어

> 클래스로 구현하여, 외부에서는 geeter와 setter로만 객체를 제어할 수 있게 하였다. 또한, 힌트와 메소드별 역할을 적은 주석을 추가하여 가독성을 높였다.

- 블로그 포스팅

    - [19236번 - 청소년 상어 (blex.me)](https://blex.me/@mildsalmon/chap-19-%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-q47-%EC%B2%AD%EC%86%8C%EB%85%84-%EC%83%81%EC%96%B4)

- GitHub Code

    - [Beajoon - 구현 - 청소년 상어 (Github)](https://github.com/mildsalmon/CodingTest-Study/commits/master/1.%20PS/1.%20%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4%20with%20%ED%8C%8C%EC%9D%B4%EC%8D%AC/Ch19/Q47_%EC%B2%AD%EC%86%8C%EB%85%84%20%EC%83%81%EC%96%B4.py)

### C. 자료구조

#### a. 해시 (Hash)

> 해시의 특성인 key-value를 이용하여 Dict 자료형의 key값을 `hash()`의 리턴값으로 주고 이름을 value로 주었다.

- 블로그 포스팅

    - [10546번 - 배부른 마라토너 (blex.me)](https://blex.me/@mildsalmon/10546%EB%B2%88-%EB%B0%B0%EB%B6%80%EB%A5%B8-%EB%A7%88%EB%9D%BC%ED%86%A0%EB%84%88)

- GitHub Code

    - [Beajoon - hash - 배부른 마라토너 (Github)](https://github.com/mildsalmon/CodingTest-Study/commits/master/1.%20PS/2.%20%EB%B0%B1%EC%A4%80/2.%20%EC%8B%A4%EB%B2%84/4/10546.py)

### D. 데이터

#### a. 크로스 집계

> 트랜잭션 테이블을 크로스 테이블로 변환하는 크로스 집계, 즉 Pivot을 진행했다.

- 블로그 포스팅

    - [Occupations (blex.me)](https://blex.me/@mildsalmon/occupations)

- GitHub Code

    - [HackerRank - pivot - Occupations (Github)](https://github.com/mildsalmon/CodingTest-Study/commits/master/2.%20SQL/2.%20HackerRank/2.%20Medium/Occupations.sql)

#### b. DAG (Directed Acyclic Graph, 방향성 비순환 그래프)

> 방향을 가지는 그래프이지만, 사이클을 생성하지 않는 그래프이다. 작업의 우선순위에 따라 선행작업을 먼저 처리한다. DAG에서는 위상 정렬을 사용하여 우선순위를 표현한다. 
> 
> 데이터 플로우에서는 DAG를 구성하는 각 노드가 모두 동시 병행으로 실행되지만, 여기서는 MapReduce처럼 하나의 노드에서 처리가 끝나지 않으면 다음 처리로 진행할 수 없다.

- 블로그 포스팅

    - [2252번 - 줄 세우기 (blex.me)](https://blex.me/@mildsalmon/2252%EB%B2%88-%EC%A4%84-%EC%84%B8%EC%9A%B0%EA%B8%B0)

- GitHub Code

    - [Beajoon - Topology_sort - 줄 세우기 (Github)](https://github.com/mildsalmon/CodingTest-Study/commits/master/1_PS/2_baekjoon_online_judge/3_Gold/3/2252.py)

