/*
Date    : 2022.01.09
Update  : 2022.01.09
Source  : New Companies.sql
Purpose : join / distinct / count
url     : https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT c.company_code, c.founder, COUNT(DISTINCT(lm.lead_manager_code)), COUNT(DISTINCT(sm.senior_manager_code)), COUNT(DISTINCT(m.manager_code)), COUNT(DISTINCT(e.employee_code))
FROM company c LEFT OUTER JOIN lead_manager lm ON c.company_code = lm.company_code
    LEFT OUTER JOIN senior_manager sm ON lm.lead_manager_code = sm.lead_manager_code
    LEFT OUTER JOIN manager m ON sm.senior_manager_code = m.senior_manager_code
    LEFT OUTER JOIN employee e ON m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder
ORDER BY company_code;