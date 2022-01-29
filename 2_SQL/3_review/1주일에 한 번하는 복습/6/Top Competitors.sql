/*
Date    : 2022.01.30
Update  : 2022.01.30
Source  : Top Competitors.sql
Purpose : JOIN / GROUP BY / ORDER BY
url     : https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT h.hacker_id,
    h.name,
    cnt
FROM (
    SELECT s.hacker_id AS id,
        COUNT(s.hacker_id) AS cnt
    FROM submissions s
        LEFT OUTER JOIN (
            SELECT c.challenge_id AS chal_id,
                d.score AS max_score
            FROM challenges c
                LEFT OUTER JOIN difficulty d
                ON (c.difficulty_level = d.difficulty_level)
        ) challenge_score
        ON (s.challenge_id = challenge_score.chal_id)
    WHERE s.score = challenge_score.max_score
    GROUP BY s.hacker_id
    HAVING COUNT(s.hacker_id) >= 2
    ORDER BY cnt DESC, id ASC
) full_score_hacker LEFT OUTER JOIN hackers h
    ON (full_score_hacker.id = h.hacker_id)
;