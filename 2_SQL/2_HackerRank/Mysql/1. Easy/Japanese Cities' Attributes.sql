/*
Date    : 2022.03.28
Update  : 2022.03.28
Source  : Japanese Cities' Attributes.sql
Purpose : WHERE
url     : https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT id, name, countrycode, district, population
FROM CITY
WHERE countrycode = 'JPN'
;