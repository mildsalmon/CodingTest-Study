/*
Date    : 2021.03.14
Update  : 2021.03.14
Source  : 아픈 동물 찾기.sql
Purpose : 조건에 맞춰서 정렬
url     : https://programmers.co.kr/learn/courses/30/lessons/59036?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY 1 ASC
;