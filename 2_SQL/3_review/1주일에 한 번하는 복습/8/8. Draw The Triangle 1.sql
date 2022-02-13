/*
Date    : 2022.02.13
Update  : 2022.02.13
Source  : Draw The Triangle 1.sql
Purpose : CONNECT BY / 계층형 질의 / RPAD
url     : https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT RPAD('*', num, ' *')
FROM (
    SELECT LEVEL AS num
    FROM dual
    CONNECT BY LEVEL <= (20 * 2)
    ORDER BY num DESC
)
WHERE MOD(num, 2) = 0
;