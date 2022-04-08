/*
Date    : 2022.04.08
Update  : 2022.04.08
Source  : Higher Than 75 Marks.sql
Purpose : WHERE / SUBSTR / ORDER BY
url     : https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT name
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTR(name, -3) ASC, ID ASC
;