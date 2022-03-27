/*
Date    : 2022.03.22
Update  : 2022.03.27
Source  : 입양 시각 구하기(2).sql
Purpose : GROUP BY / CASTING / HAVING / SET(사용자 변수)
url     : https://programmers.co.kr/learn/courses/30/lessons/59413?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

set @hour := -1;

SELECT A.hour
     , IFNULL(B.cnt, 0)
FROM (
    SELECT @hour := @hour + 1 AS hour
    FROM ANIMAL_OUTS
    WHERE @hour < 23
) A LEFT JOIN (
    SELECT HOUR(DATETIME) AS hour
         , COUNT(1) AS cnt
    FROM ANIMAL_OUTS
    GROUP BY 1
) B ON (A.hour = B.hour)
;