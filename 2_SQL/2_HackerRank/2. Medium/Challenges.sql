/*
Date    : 2022.01.24
Update  : 2022.01.24
Source  : Challenges.sql
Purpose : 서브쿼리 /
url     : https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT h.hacker_id, h.name, COUNT(c.challenge_id)
FROM Hackers h JOIN Challenges c ON (h.hacker_id = c.hacker_id)
GROUP BY h.hacker_id, h.name
ORDER BY COUNT(c.challenge_id), h.hacker_id
;