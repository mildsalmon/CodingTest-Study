/*
Date    : 2022.04.08
Update  : 2022.04.09
Source  : The PADS.sql
Purpose : SELECT / CASE WHEN / CONCAT
url     : https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/
SELECT CONCAT(name, '(', SUBSTR(occupation, 1, 1), ')')
FROM occupations
ORDER BY 1
;
SELECT CONCAT('There are a total of ', COUNT(name),' ', LOWER(occupation), 's.')
FROM occupations
GROUP BY occupation
ORDER BY 1
;