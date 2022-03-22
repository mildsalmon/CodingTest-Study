/*
Date    : 2022.03.22
Update  : 2022.03.22
Source  : 고양이와 개는 몇 마리 있을까.sql
Purpose : COUNT
url     : https://programmers.co.kr/learn/courses/30/lessons/59040?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_TYPE
     , COUNT(1)
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY 1
ORDER BY 1 ASC
;