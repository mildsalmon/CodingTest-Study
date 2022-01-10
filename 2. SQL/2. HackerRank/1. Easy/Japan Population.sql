/*
Date    : 2022.01.10
Update  : 2022.01.10
Source  : Japan Population.sql
Purpose : sum
url     : https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT SUM(population)
FROM CITY
WHERE countrycode = 'JPN';