/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : DATETIME에서 DATE로 형 변환.sql
Purpose : LEFT / DATETIME / DATE
url     : https://programmers.co.kr/learn/courses/30/lessons/59414?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , NAME
     , LEFT(DATETIME, 10)
FROM ANIMAL_INS
ORDER BY 1
;