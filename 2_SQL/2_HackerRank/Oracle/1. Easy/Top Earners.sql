/*
Date    : 2022.01.12
Update  : 2022.01.12
Source  : Top Earners.sql
Purpose : count / 서브쿼리
url     : https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

-- count를 사용할때 다른 절이 있으면 다른 절들을 group by로 묶어줘야한다.
SELECT a.months*a.salary, COUNT(a.months*a.salary)
FROM employee a
WHERE a.months*a.salary = (SELECT MAX(b.months*b.salary)
                      FROM employee b)
GROUP BY a.months*a.salary
;