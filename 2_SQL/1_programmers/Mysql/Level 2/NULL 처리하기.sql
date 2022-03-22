/*
Date    : 2022.03.23
Update  : 2022.03.23
Source  : NULL 처리하기.sql
Purpose : NULL
url     : https://programmers.co.kr/learn/courses/30/lessons/59410?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_TYPE
     , IFNULL(NAME, "No name")
     , SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
;