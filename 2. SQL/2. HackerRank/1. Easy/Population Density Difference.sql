/*
Date    : 2022.01.10
Update  : 2022.01.10
Source  : Population Density Difference.sql
Purpose : max / min
url     : https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT MAX(population) - MIN(population)
FROM city;