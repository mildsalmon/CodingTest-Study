/*
Date    : 2022.01.19
Update  : 2022.01.19
Source  : African Cities.sql
Purpose : join / sum
url     : https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ci.name
FROM city ci LEFT OUTER JOIN country co ON (ci.countrycode = co.code)
WHERE co.continent = 'Africa'
;