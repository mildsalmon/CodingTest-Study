/*
Date    : 2021.03.14
Update  : 2021.03.14
Source  : 역순 정렬하기.sql
Purpose : 조건에 맞춰서 정렬
url     : https://programmers.co.kr/learn/courses/30/lessons/59035?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT NAME
     , DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
;