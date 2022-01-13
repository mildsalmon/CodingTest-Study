/*
Date    : 2022.01.13
Update  : 2022.01.13
Source  : Weather Observation Station 16.sql
Purpose : ROUND / MIN
url     : https://www.hackerrank.com/challenges/weather-observation-station-16/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(MIN(lat_n), 4)
FROM station
WHERE lat_n > 38.7789
;