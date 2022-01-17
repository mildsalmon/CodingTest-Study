/*
Date    : 2022.01.17
Update  : 2022.01.17
Source  : Weather Observation Station 18.sql
Purpose : manhattan distance / round / min / max
url     : https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND((MAX(lat_n) - MIN(lat_n)) + (MAX(long_w) - MIN(long_w)), 4)
FROM station
;