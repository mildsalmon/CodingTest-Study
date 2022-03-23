/*
Date    : 2022.03.23
Update  : 2022.03.23
Source  : 없어진 기록 찾기.sql
Purpose : RIGHT JOIN / OUTER JOIN / NULL
url     : https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT O.ANIMAL_ID
     , O.NAME
FROM ANIMAL_INS I RIGHT OUTER JOIN ANIMAL_OUTS O ON (I.ANIMAL_ID = O.ANIMAL_ID)
WHERE I.ANIMAL_ID IS NULL
ORDER BY 1
;
