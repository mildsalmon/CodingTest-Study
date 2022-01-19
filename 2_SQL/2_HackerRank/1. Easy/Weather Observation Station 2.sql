/*
Date    : 2022.01.12
Update  : 2022.01.12
Source  : Weather Observation Station 2.sql
Purpose : ROUND / SUM
url     : https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM station
;