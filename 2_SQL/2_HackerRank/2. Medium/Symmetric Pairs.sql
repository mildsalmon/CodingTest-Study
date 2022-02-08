/*
Date    : 2022.02.08
Update  : 2022.02.08
Source  : Symmetric Pairs.sql
Purpose : JOIN / GROUP BY / HAVING
url     : https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT a.x, a.y
FROM functions a
JOIN functions b ON (a.x = b.y
                    AND a.y = b.x)
GROUP BY a.x, a.y
HAVING ((a.x = a.y
        AND COUNT(a.x) >= 2)
    OR (a.x != a.y
        AND COUNT(a.x) >= 1))
    AND a.x <= a.y
ORDER BY a.x ASC
;