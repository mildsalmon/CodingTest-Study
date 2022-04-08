/*
Date    : 2022.04.08
Update  : 2022.04.08
Source  : Employee Salaries.sql
Purpose : SELECT / ORDER BY / WHERE
url     : https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT name
FROM employee
WHERE salary > 2000
    AND months < 10
ORDER BY employee_id ASC
;