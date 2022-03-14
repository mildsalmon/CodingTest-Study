/*
Date    : 2021.03.14
Update  : 2021.03.14
Source  : 여러 기준으로 정렬하기.sql
Purpose : 조건에 맞춰서 정렬
url     : https://programmers.co.kr/learn/courses/30/lessons/59404?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , NAME
     , DATETIME
FROM ANIMAL_INS
ORDER BY 2 ASC, 3 DESC
;