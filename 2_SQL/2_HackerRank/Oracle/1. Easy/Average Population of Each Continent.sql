/*
Date    : 2022.01.19
Update  : 2022.01.19
Source  : Average Population of Each Continent.sql
Purpose : join / sum / FLOOR / Group by
url     : https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT co.continent, FLOOR(AVG(ci.population))
FROM city ci JOIN country co ON (ci.countrycode = co.code)
GROUP BY co.continent
;