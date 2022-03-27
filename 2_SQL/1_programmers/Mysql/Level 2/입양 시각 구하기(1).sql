/*
Date    : 2022.03.22
Update  : 2022.03.27
Source  : 입양 시각 구하기(1).sql
Purpose : GROUP BY / CASTING / HAVING
url     : https://programmers.co.kr/learn/courses/30/lessons/59412?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT HOUR(DATETIME)
     , COUNT(1)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9
     AND HOUR(DATETIME) < 20
GROUP BY 1
ORDER BY 1
;