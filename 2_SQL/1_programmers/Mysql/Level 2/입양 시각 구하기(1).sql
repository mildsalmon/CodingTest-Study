/*
Date    : 2022.03.22
Update  : 2022.03.22
Source  : 입양 시각 구하기(1).sql
Purpose : GROUP BY / CASTING / HAVING
url     : https://programmers.co.kr/learn/courses/30/lessons/59412?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT HOUR(DATETIME) AS DATE
     , COUNT(1)
FROM ANIMAL_OUTS
GROUP BY 1
HAVING DATE >= 9 AND DATE < 20
ORDER BY 1
;