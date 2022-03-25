/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 헤비 유저가 소유한 장소.sql
Purpose : 서브 쿼리 / GROUP BY / HAVING
url     : https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ID
     , NAME
     , HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
    ORDER BY 1
)
;