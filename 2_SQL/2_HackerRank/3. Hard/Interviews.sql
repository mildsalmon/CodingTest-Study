/*
Date    : 2022.02.14
Update  : 2022.03.04
Source  : Interviews.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.contest_id
     , A.hacker_id
     , A.name
     , SUM(E.t_s)
     , SUM(E.t_a_s)
     , SUM(D.t_v)
     , SUM(D.t_u_v)
FROM contests A
JOIN colleges B ON (A.contest_id = B.contest_id)
JOIN challenges C ON (B.college_id = C.college_id)
LEFT JOIN (
    SELECT challenge_id
         , SUM(total_views) AS t_v
         , SUM(total_unique_views) AS t_u_v
    FROM view_stats
    GROUP BY challenge_id
) D ON (C.challenge_id = D.challenge_id)
LEFT JOIN (
    SELECT challenge_id
         , SUM(total_submissions) AS t_s
         , SUM(total_accepted_submissions) AS t_a_s
    FROM submission_stats
    GROUP BY challenge_id
) E ON (C.challenge_id = E.challenge_id)
WHERE D.t_v + D.t_u_v + E.t_s + E.t_a_s > 0
GROUP BY A.contest_id, A.hacker_id, A.name
ORDER BY A.contest_id ASC
;