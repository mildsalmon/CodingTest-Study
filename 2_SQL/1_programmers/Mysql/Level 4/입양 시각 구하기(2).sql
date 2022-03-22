/*
Date    : 2022.03.22
Update  : 2022.03.22
Source  : 입양 시각 구하기(2).sql
Purpose : GROUP BY / CASTING / HAVING / SET(사용자 변수)
url     : https://programmers.co.kr/learn/courses/30/lessons/59413?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

set @hour := -1;

SELECT @hour := @hour + 1
     , (SELECT COUNT(*)
        FROM ANIMAL_OUTS
        WHERE @hour = HOUR(DATETIME))
FROM ANIMAL_OUTS
WHERE @hour <= 22
ORDER BY 1
;