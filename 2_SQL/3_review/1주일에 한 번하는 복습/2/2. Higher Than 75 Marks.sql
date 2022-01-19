/*
Date    : 2022.01.01
Update  : 2022.01.01
Source  : Higher Than 75 Marks.sql
Purpose : 단순 where / order by
url     : https://www.hackerrank.com/challenges/more-than-75-marks/problem
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT name
FROM STUDENTS
WHERE marks > 75
ORDER BY SUBSTR(name, -3) ASC, id ASC;