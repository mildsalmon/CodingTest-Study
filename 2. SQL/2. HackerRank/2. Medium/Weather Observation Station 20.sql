/*
Date    : 2022.01.17
Update  : 2022.01.17
Source  : Weather Observation Station 20.sql
Purpose : 중앙값 / MEDIAN
url     : https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(MEDIAN(lat_n), 4)
FROM station
;