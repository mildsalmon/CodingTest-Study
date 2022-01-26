/*
Date    : 2022.01.25
Update  : 2022.01.25
Source  : Top Competitors.sql
Purpose : JOIN / 서브쿼리
url     : https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT H.hacker_id,
       H.name
FROM (
    SELECT DISTINCT(S.hacker_id) AS hacker_id,
           COUNT(*) OVER (PARTITION BY S.hacker_id) AS id_count
    FROM Submissions S
        LEFT OUTER JOIN (
            SELECT C.challenge_id AS C_id,
                   D.score AS max_score
            FROM Challenges C
                LEFT OUTER JOIN Difficulty D
                    ON (D.difficulty_level = C.difficulty_level)
        ) NC
            ON (S.challenge_id = NC.C_id)
    WHERE S.score = NC.max_score
) NH
    LEFT OUTER JOIN Hackers H
        ON (NH.hacker_id = H.hacker_id)
WHERE NH.id_count >= 2
ORDER BY id_count DESC, hacker_id ASC
;