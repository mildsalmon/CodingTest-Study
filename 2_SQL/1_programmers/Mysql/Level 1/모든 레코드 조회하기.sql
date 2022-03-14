/*
Date    : 2021.03.14
Update  : 2021.03.14
Source  : 모든 레코드 조회하기.sql
Purpose : 조건에 맞춰서 정렬
url     : https://programmers.co.kr/learn/courses/30/lessons/59034?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , ANIMAL_TYPE
     , DATETIME
     , INTAKE_CONDITION
     , NAME
     , SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY 1 ASC
;