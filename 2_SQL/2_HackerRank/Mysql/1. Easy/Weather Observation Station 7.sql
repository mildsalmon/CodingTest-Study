/*
Date    : 2022.04.06
Update  : 2022.04.06
Source  : Weather Observation Station 7.sql
Purpose : SELECT / DISTINCT / SUBSTR / IN
url     : https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT DISTINCT(city)
FROM station
WHERE SUBSTR(city, -1, 1) IN ('a', 'e', 'i', 'o', 'u')
;