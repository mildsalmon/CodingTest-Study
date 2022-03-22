/*
Date    : 2022.03.22
Update  : 2022.03.22
Source  : 동명 동물 수 찾기.sql
Purpose : GROUP BY / COUNT / HAVING
url     : https://programmers.co.kr/learn/courses/30/lessons/59041?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT NAME
     , COUNT(1)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY 1
HAVING COUNT(1) >= 2
ORDER BY 1
;