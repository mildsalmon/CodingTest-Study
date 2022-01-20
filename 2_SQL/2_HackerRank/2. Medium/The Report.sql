/*
Date    : 2022.01.20
Update  : 2022.01.20
Source  : The Report.sql
Purpose : LEFT OUTER JOIN / 비등가 조인(범위 조인) / CASE
url     : https://www.hackerrank.com/challenges/the-report?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT CASE WHEN g.grade >= 8 THEN s.name END,
        g.grade, s.marks
FROM students s LEFT OUTER JOIN grades g ON (s.marks BETWEEN g.min_mark AND g.max_mark)
ORDER BY g.grade DESC, s.name ASC, s.marks ASC
;