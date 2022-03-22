/*
Date    : 2022.03.14
Update  : 2022.03.14
Source  : 상위 n개 레코드.sql
Purpose : 조건에 맞춰서 정렬
url     : https://programmers.co.kr/learn/courses/30/lessons/59405?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1
;