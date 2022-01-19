/*
Date    : 2022.01.12
Update  : 2022.01.12
Source  : Weather Observation Station 13.sql
Purpose : TRUNC / BETWEEN
url     : https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT TRUNC(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N BETWEEN 38.7880 AND 137.2345
;