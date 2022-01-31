/*
Date    : 2022.01.31
Update  : 2022.01.31
Source  : Contest Leaderboard.sql
Purpose : JOIN / 인라인 뷰 / GROUP BY
url     : https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT h.hacker_id,
    h.name,
    SUM(score) AS total_score
FROM (
    SELECT hacker_id,
        challenge_id,
        MAX(score) AS score
    FROM submissions
    GROUP BY hacker_id, challenge_id
) s LEFT OUTER JOIN hackers h
ON (s.hacker_id = h.hacker_id)
WHERE score != 0
GROUP BY h.hacker_id, h.name
ORDER BY total_score DESC, hacker_id ASC
;