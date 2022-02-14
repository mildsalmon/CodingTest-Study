/*
Date    : 2022.02.14
Update  : 2022.02.14
Source  : Interviews.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.contest_id,
       A.hacker_id,
       A.name,
       SUM(ss.total_submissions),
       SUM(ss.total_accepted_submissions),
       SUM(vs.total_views),
       SUM(vs.total_unique_views)
FROM contests A
JOIN colleges B ON (A.contest_id = B.contest_id)
JOIN challenges C ON (B.college_id = C.college_id)
LEFT OUTER JOIN (
    SELECT challenge_id,
           SUM(total_views) AS total_views,
           SUM(total_unique_views) AS total_unique_views
    FROM view_stats
    GROUP BY challenge_id
) vs ON (C.challenge_id = vs.challenge_id)
LEFT OUTER JOIN (
    SELECT challenge_id,
           SUM(total_submissions) AS total_submissions,
           SUM(total_accepted_submissions) AS total_accepted_submissions
    FROM submission_stats
    GROUP BY challenge_id
) ss ON (C.challenge_id = ss.challenge_id)
GROUP BY A.contest_id, A.hacker_id, A.name
ORDER BY A.contest_id ASC
;