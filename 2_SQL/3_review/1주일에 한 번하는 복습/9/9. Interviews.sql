/*
Date    : 2022.02.28
Update  : 2022.02.28
Source  : Interviews.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.contest_id
     , A.hacker_id
     , A.name
     , SUM(E.t_submissions)
     , SUM(E.t_a_submissions)
     , SUM(D.t_views)
     , SUM(D.t_u_views)
FROM contests A
JOIN colleges B ON (A.contest_id = B.contest_id)
JOIN challenges C ON (B.college_id = C.college_id)
LEFT OUTER JOIN (
    SELECT challenge_id
         , SUM(total_views) AS t_views
         , SUM(total_unique_views) AS t_u_views
    FROM view_stats
    GROUP BY challenge_id
) D ON (C.challenge_id = D.challenge_id)
LEFT OUTER JOIN (
    SELECT challenge_id
         , SUM(total_submissions) AS t_submissions
         , SUM(total_accepted_submissions) AS t_a_submissions
    FROM submission_stats
    GROUP BY challenge_id
) E ON (C.challenge_id = E.challenge_id)
GROUP BY A.contest_id, A.hacker_id, A.name
HAVING SUM(E.t_submissions) + SUM(E.t_a_submissions) + SUM(D.t_views) + SUM(D.t_u_views) > 0
ORDER BY A.contest_id ASC
;