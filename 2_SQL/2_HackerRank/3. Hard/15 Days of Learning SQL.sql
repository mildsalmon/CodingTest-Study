/*
Date    : 2022.02.18
Update  : 2022.02.18
Source  : 15 Days of Learning SQL.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT B.s_date
     , A.cnt
     , hackers.hacker_id
     , hackers.name
FROM (
    SELECT s.submission_date AS s_date
         , COUNT(DISTINCT(s.hacker_id)) AS cnt
    FROM submissions s
    WHERE (s.submission_date - TO_DATE('2016-03-01')) = (
        SELECT COUNT(DISTINCT(ss.submission_date))
        FROM submissions ss
        WHERE s.submission_date > ss.submission_date
            AND s.hacker_id = ss.hacker_id
    )
    GROUP BY s.submission_date
) A JOIN (
    SELECT s_date
         , id
         , ROW_NUMBER() OVER(PARTITION BY s_date
                            ORDER BY cnt DESC,
                                     id ASC) AS num
    FROM (
        SELECT s.submission_date AS s_date
             , s.hacker_id AS id
             , COUNT(s.hacker_id) AS cnt
        FROM submissions s
        GROUP BY s.submission_date, s.hacker_id
    )
) B ON (B.num = 1
       AND A.s_date = B.s_date)
JOIN hackers ON (B.id = hackers.hacker_id)
ORDER BY B.s_date ASC
;