/*
Date    : 2022.04.06
Update  : 2022.04.06
Source  : Weather Observation Station 5.sql
Purpose : SELECT / LIMIT / UNION / ORDER BY / LENGTH
url     : https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

(SELECT city, LENGTH(city)
FROM station
ORDER BY 2, 1
LIMIT 1)
UNION
(SELECT city, LENGTH(city)
FROM station
ORDER BY 2 DESC, 1
LIMIT 1)
;