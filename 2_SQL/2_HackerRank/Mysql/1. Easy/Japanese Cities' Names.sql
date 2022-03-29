/*
Date    : 2022.03.29
Update  : 2022.03.29
Source  : Japanese Cities' Name.sql
Purpose : WHERE
url     : https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT name
FROM CITY
WHERE countrycode = 'JPN'
;