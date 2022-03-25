/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 오랜 기간 보호한 동물(2).sql
Purpose : DATE 뺄셈 / RIGHT JOIN / LIMIT
url     : https://programmers.co.kr/learn/courses/30/lessons/59411?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT B.ANIMAL_ID
     , B.NAME
FROM ANIMAL_INS A RIGHT JOIN ANIMAL_OUTS B ON (A.ANIMAL_ID = B.ANIMAL_ID)
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2
;