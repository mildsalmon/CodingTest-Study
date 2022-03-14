/*
Date    : 2022.01.17
Update  : 2022.01.17
Source  : Weather Observation Station 20.sql
Purpose : 중앙값 / MEDIAN / window function / count / row_number / ceil / floor / avg / round
url     : https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

/*
 중앙값
    row의 수가 홀수일때
        index가 1부터 시작하기 때문에, 총 row의 수 + 1 / 2 = 중앙값의 index
    row의 수가 짝수일때
        총 row의 수 + 1 / 2의 올림, 내림 = 중앙값의 index

    ===

    row의 수가 홀수
        10, 20, 30, 40, 50
            (5 + 1) / 2 = 3
    row의 수가 짝수
        10, 20, 30, 40
            (4 + 1) / 2의 올림, 내림 = 3, 2

 */

SELECT ROUND(AVG(LAT_N), 4)
FROM (
    SELECT LAT_N
         , ROW_NUMBER() OVER(ORDER BY LAT_N ASC) AS rank
         , COUNT(1) OVER() AS cnt
    FROM station
)
WHERE rank IN ((cnt + 1)/2, (cnt+1)/2+MOD((cnt+1),2))
;