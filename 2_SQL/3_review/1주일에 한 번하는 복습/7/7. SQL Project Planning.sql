/*
Date    : 2022.02.06
Update  : 2022.02.06
Source  : SQL Project Planning.sql
Purpose : JOIN / 인라인 뷰 / date 뺄셈
url     : https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT C.start_date,
    D.end_date
FROM (
    SELECT ROW_NUMBER() OVER(ORDER BY B.start_date) AS C_num,
        B.start_date AS start_date
    FROM projects A
    RIGHT OUTER JOIN projects B ON (A.end_date = B.start_date)
    WHERE A.end_date IS NULL
) C
LEFT OUTER JOIN (
    SELECT ROW_NUMBER() OVER (ORDER BY A.end_date) AS D_num,
        A.end_date AS end_date
    FROM projects A
    LEFT OUTER JOIN projects B ON (A.end_date = B.start_date)
    WHERE B.start_date IS NULL
) D ON (C.C_num = D.D_num)
ORDER BY (D.end_date - C.start_date) ASC, C.start_date ASC
;