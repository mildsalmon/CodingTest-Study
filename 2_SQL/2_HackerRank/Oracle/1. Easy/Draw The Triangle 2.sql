/*
Date    : 2022.02.11
Update  : 2022.02.11
Source  : Draw The Triangle 2.sql
Purpose : RPAD / CONNECT BY / LEVEL
url     : https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT RPAD('*', num, ' *')
FROM (
    SELECT LEVEL AS num
    FROM DUAL
    CONNECT BY LEVEL <= (20 * 2)
)
WHERE MOD(num, 2) = 0
;