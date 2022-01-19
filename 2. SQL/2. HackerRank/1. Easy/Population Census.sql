/*
Date    : 2022.01.19
Update  : 2022.01.19
Source  : Population Census.sql
Purpose : join / sum
url     : https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT SUM(ci.population)
FROM city ci JOIN country co ON (ci.countrycode = co.code)
WHERE co.continent = 'Asia';