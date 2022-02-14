/*
Date    : 2022.02.14
Update  : 2022.02.14
Source  : Interviews.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT D.contest_id,
       D.hacker_id,
       D.name,
       C.total_submissions,
       C.total_accepted_submissions,
       C.total_views,
       C.total_unique_views
FROM (
    SELECT D.contest_id AS contest_id,
           SUM(A.total_views) AS total_views,
           SUM(A.total_unique_views) AS total_unique_views,
           SUM(B.total_submissions) AS total_submissions,
           SUM(B.total_accepted_submissions) AS total_accepted_submissions
    FROM (
        SELECT challenge_id,
               SUM(total_views) AS total_views,
               SUM(total_unique_views) AS total_unique_views
        FROM view_stats
        GROUP BY challenge_id
    ) A JOIN (
        SELECT challenge_id,
               SUM(total_submissions) AS total_submissions,
               SUM(total_accepted_submissions) AS total_accepted_submissions
        FROM submission_stats
        GROUP BY challenge_id
    ) B ON (A.challenge_id = B.challenge_id)
    JOIN challenges C ON (A.challenge_id = C.challenge_id)
    JOIN colleges D ON (C.college_id = D.college_id)
    WHERE A.total_views + A.total_unique_views + B.total_submissions + B.total_accepted_submissions != 0
    GROUP BY D.contest_id
) C JOIN contests D ON (C.contest_id = D.contest_id)
ORDER BY D.contest_id ASC
;