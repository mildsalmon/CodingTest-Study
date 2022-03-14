/*
Date    : 2022.02.18
Update  : 2022.03.10
Source  : 15 Days of Learning SQL.sql
Purpose : JOIN
url     : https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT X.submission_date
     , X.cnt
     , Y.hacker_id
     , Z.name
FROM (
    SELECT A.submission_date
         , COUNT(DISTINCT A.hacker_id) AS cnt
    FROM submissions A
    WHERE (A.submission_date - TO_DATE('2016-03-01')) = (
        SELECT COUNT(DISTINCT B.submission_date)
        FROM submissions B
        WHERE A.submission_date > B.submission_date
            AND A.hacker_id = B.hacker_id
    )
    GROUP BY A.submission_date
) X LEFT JOIN (
    SELECT D.submission_date
         , D.hacker_id
         , ROW_NUMBER() OVER(PARTITION BY D.submission_date ORDER BY D.cnt DESC, D.hacker_id ASC) AS rank
    FROM (
        SELECT C.submission_date
             , C.hacker_id
             , COUNT(1) AS cnt
        FROM submissions C
        GROUP BY C.submission_date, C.hacker_id
    ) D
) Y ON (Y.rank = 1 AND X.submission_date = Y.submission_date)
JOIN hackers Z ON (Y.hacker_id = Z.hacker_id)
ORDER BY 1
;