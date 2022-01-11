/*
Date    : 2022.01.11
Update  : 2022.01.11
Source  : The Blunder.sql
Purpose : ceil / avg / replace
url     : https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT CEIL(AVG(salary) - AVG(REPLACE(salary, '0', '')))
FROM EMPLOYEES
;