/*
Date    : 2022.02.07
Update  : 2022.02.07
Source  : Placements.sql
Purpose : JOIN / 인라인 뷰
url     : https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT s.name
FROM friends f
    JOIN packages p ON (f.friend_id = p.id)
    LEFT OUTER JOIN packages o_p ON (f.id = o_p.id
                                    AND o_p.salary < p.salary)
    LEFT OUTER JOIN students s ON (s.id = f.id)
WHERE o_p.id IS NOT NULL
ORDER BY p.salary ASC
;