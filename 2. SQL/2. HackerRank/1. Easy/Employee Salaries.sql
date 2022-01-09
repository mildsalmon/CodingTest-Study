/*
Date    : 2021.12.28
Update  : 2021.12.28
Source  : Employee Salaries.sql
Purpose : 조건에 맞춰서 정렬
url     : https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/
SELECT name
FROM employee
WHERE salary > 2000 AND months < 10
ORDER BY employee_id ASC;