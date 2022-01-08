/*
Date    : 2021.12.28
Update  : 2021.12.28
Source  : Type of Triangle.sql
Purpose : 삼각형 성립 조건에 맞춰서 풀었다.
url     : https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

/*
 삼각형의 성립 조건
    한 변의 길이가 나머지 두 변의 길이 합보다 작아야 한다.
    즉, A=1, B=2, C=3인 경우는 삼각형이 될 수 없다.
    마찬가지로, A=1, B=2, C=4인 경우도 삼각형이 될 수 없다.

 따라서 아래 순서로 각 변의 길이를 구했다.
    1. 삼각형이 불가능한 경우
    2. 세변의 길이가 다른 경우
    3. 두 변의 길이가 같을 경우
    4. 모든 변의 길이가 같을 경우

 오라클에서는 CASE ~ WHEN ~ THEN ~
            END 문으로 조건을 줄 수 있다.

 나도 이렇게까지 조건을 줄 수 있으리라 생각하지는 않았는데,
 생각해보니 WHEN절에 들어가는 구문은 결국 TRUE, FALSE가 나와야 하므로 조건이 수십개여도 상관없겠다.

 ---

 각 삼각형을 WHERE절에 조건으로 주고 UNION으로 묶을 수도 있겠지만,
 문제에 ORDER BY을 어떤 방식으로 하라는지 나와있지는 않아서 틀릴 수도 있겠다.
 오히려 각 WHERE절이 점점 커지는 방식이 되어 더 복잡해질 수 있겠다.
    EX) 1번 삼각형의 WHERE절 = A + B <= C OR A + C <= B OR B + C <= A
        2번 삼각형의 WHERE절 = NOT (A + B <= C OR A + C <= B OR B + C <= A)
                             AND (A != B AND B != C AND A != C THEN 'Scalene')
        3번 삼각형의 WHERE절 = NOT (A + B <= C OR A + C <= B OR B + C <= A)
                             NOT (A != B AND B != C AND A != C)
                             AND (A != B OR B != C OR A != C)
        4번 삼각형의 WHERE절 = NOT (A + B <= C OR A + C <= B OR B + C <= A)
                             NOT (A != B AND B != C AND A != C)
                             NOT (A != B OR B != C OR A != C)
                             AND (A = B AND B = C)
 왜 이렇게 하냐면, 상위 조건에서 FALSE인 것이 하위 조건으로 내려가서 구해지기 때문이다.
    2번 삼각형을 구하는 WHERE절에서 첫번째 조건이 없다면, A=1, B=2, C=10인 경우 'Not A Triangle'이 아닌 'Scalene'가 나올 것이다.
 */

SELECT CASE WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
            WHEN A != B AND B != C AND A != C THEN 'Scalene'
            WHEN A != B OR B != C OR A != C THEN 'Isosceles'
            WHEN A = B AND B = C THEN 'Equilateral'
        END
FROM TRIANGLES;