/*
Date    : 2022.01.31
Update  : 2022.01.31
Source  : SQL Project Planning.sql
Purpose : JOIN / 인라인 뷰 / date 뺄셈
url     : https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT s_date.start_date,
    e_date.end_date
FROM (
    SELECT ROW_NUMBER() OVER (ORDER BY A.start_date ASC) AS num,
        A.start_date
    FROM projects A
        LEFT OUTER JOIN projects B
        ON (A.start_date = B.end_date)
    WHERE B.start_date IS NULL
) s_date
LEFT OUTER JOIN (
    SELECT ROW_NUMBER() OVER (ORDER BY A.end_date ASC) AS num,
        A.end_date
    FROM projects A
        LEFT OUTER JOIN projects C
        ON (A.end_date = C.start_date)
    WHERE C.end_date IS NULL
) e_date
ON (s_date.num = e_date.num)
ORDER BY e_date.end_date - s_date.start_date ASC, s_date.start_date ASC
;