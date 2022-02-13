/*
Date    : 2022.02.13
Update  : 2022.02.13
Source  : Placements.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.name
FROM (SELECT s.id AS id,
            s.name AS name,
            p.salary AS salary
      FROM students s
      LEFT OUTER JOIN packages p ON (s.id = p.id)
      ) A
    LEFT OUTER JOIN (SELECT f.id AS id,
                            f.friend_id AS f_id,
                            p.salary AS salary
                     FROM friends f
                     LEFT OUTER JOIN packages p ON (f.friend_id = p.id)
                     ) B ON (A.id = B.id)
WHERE A.salary < B.salary
ORDER BY B.salary ASC
;