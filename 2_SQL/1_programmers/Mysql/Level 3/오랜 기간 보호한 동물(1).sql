/*
Date    : 2022.03.23
Update  : 2022.03.23
Source  : 오랜기간 보호한 동물(1).sql
Purpose : LEFT JOIN / OUTER JOIN / NULL / LIMIT
url     : https://programmers.co.kr/learn/courses/30/lessons/59044?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT I.NAME
     , I.DATETIME
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O ON (I.ANIMAL_ID = O.ANIMAL_ID)
WHERE O.ANIMAL_ID IS NULL
ORDER BY 2
LIMIT 3
;