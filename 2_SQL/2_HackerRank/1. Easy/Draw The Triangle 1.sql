/*
Date    : 2022.02.09
Update  : 2022.02.09
Source  : Draw The Triangle 1.sql
Purpose : RPAD / CONNECT BY / LEVEL
url     : https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

select rpad('*', x,' *')
from(
    SELECT LEVEL x
    FROM DUAL
    CONNECT BY LEVEL <= 20 * 2
    Order by Level desc
)
WHERE mod(x, 2) = 0
;