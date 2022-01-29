/*
Date    : 2022.01.30
Update  : 2022.01.30
Source  : Challenges.sql
Purpose : PARTITION BY / GROUP BY / 인라인 뷰 / JOIN
url     : https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT h.hacker_id,
    h.name,
    c.cnt
FROM (
    SELECT hacker_id,
        COUNT(*) AS cnt,
        COUNT(*) OVER (PARTITION BY COUNT(*)) AS cnt_cnt,
        MAX(COUNT(*)) OVER () AS max_cnt
    FROM challenges
    GROUP BY hacker_id
) c LEFT OUTER JOIN hackers h
    ON (c.hacker_id = h.hacker_id)
WHERE c.cnt_cnt = 1
    OR c.cnt = c.max_cnt
ORDER BY c.cnt DESC, c.hacker_id
;