/*
Date    : 2022.01.03
Update  : 2022.01.03
Source  : New Companies.sql
Purpose : group by / left outer join / distinct / count
url     : https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT c.company_code, c.founder, COUNT(DISTINCT e.lead_manager_code), COUNT(DISTINCT e.senior_manager_code), COUNT(DISTINCT e.manager_code), COUNT(DISTINCT(employee_code))
FROM company c LEFT OUTER JOIN employee e ON (c.company_code = e.company_code)
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;