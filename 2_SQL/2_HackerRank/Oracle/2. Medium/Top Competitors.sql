/*
Date    : 2022.01.25
Update  : 2022.03.04
Source  : Top Competitors.sql
Purpose : JOIN / 서브쿼리
url     : https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT D.hacker_id
     , E.name
FROM (
    SELECT C.hacker_id
         , COUNT(DISTINCT C.challenge_id) AS cnt
    FROM challenges A
    LEFT OUTER JOIN difficulty B ON (A.difficulty_level = B.difficulty_level)
    LEFT OUTER JOIN submissions C ON (A.challenge_id = C.challenge_id)
    WHERE C.score / B.score = 1
    GROUP BY C.hacker_id
) D LEFT OUTER JOIN hackers E ON (D.hacker_id = E.hacker_id)
WHERE D.cnt > 1
ORDER BY D.cnt DESC, D.hacker_id ASC
;
