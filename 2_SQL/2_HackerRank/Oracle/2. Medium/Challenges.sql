/*
Date    : 2022.01.24
Update  : 2022.01.24
Source  : Challenges.sql
Purpose : 서브쿼리 / 인라인뷰 / group by / window 함수
url     : https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT
    sub.hacker_id,
    sub.name,
    sub.c_count
FROM (
    SELECT
        h.hacker_id AS hacker_id,
        h.name AS name,
        COUNT(*) AS c_count,
        COUNT(*) OVER (PARTITION BY COUNT(*)) AS same_number,
        MAX(COUNT(*)) OVER () AS max_number
    FROM hackers h
        JOIN challenges c
        ON (h.hacker_id = c.hacker_id)
    GROUP BY h.hacker_id, h.name
    ) sub
WHERE sub.same_number = 1
    OR sub.max_number = sub.c_count
ORDER BY sub.c_count DESC,
        sub.hacker_id ASC
;