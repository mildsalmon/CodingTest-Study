/*
Date    : 2022.03.23
Update  : 2022.03.23
Source  : 이름이 없는 동물의 아이디.sql
Purpose : NULL
url     : https://programmers.co.kr/learn/courses/30/lessons/59039?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY 1
;