/*
Date    : 2022.01.13
Update  : 2022.01.13
Source  : Weather Observation Station 14.sql
Purpose : TRUNC / MAX
url     : https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT TRUNC(MAX(lat_n), 4)
FROM station
WHERE lat_n < 137.2345
;