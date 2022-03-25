/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 이름에 el이 들어가는 동물 찾기.sql
Purpose : LIKE
url     : https://programmers.co.kr/learn/courses/30/lessons/59047?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , NAME
FROM ANIMAL_INS
WHERE LOWER(NAME) LIKE '%el%'
    AND ANIMAL_TYPE = 'Dog'
ORDER BY 2 ASC
;