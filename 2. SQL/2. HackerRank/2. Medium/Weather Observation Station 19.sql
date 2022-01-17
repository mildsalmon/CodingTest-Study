/*
Date    : 2022.01.17
Update  : 2022.01.17
Source  : Weather Observation Station 19.sql
Purpose : euclidean distance / power / sqrt / round / max / min
url     : https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(SQRT(POWER(MAX(lat_n) - MIN(lat_n) , 2) + POWER(MAX(long_w) - MIN(long_w), 2)), 4)
FROM station
;