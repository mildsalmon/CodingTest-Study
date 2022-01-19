/*
Date    : 2022.01.15
Update  : 2022.01.15
Source  : Top Earners.sql
Purpose : count / 서브쿼리
url     : https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT salary * months, COUNT(salary * months)
FROM employee
WHERE salary * months = (SELECT MAX(salary * months)
                        FROM employee)
GROUP BY salary * months
;