/*
Date    : 2022.04.05
Update  : 2022.04.05
Source  : Weather Observation Station 3.sql
Purpose : SELECT / MOD
url     : https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT DISTINCT(city)
FROM station
WHERE MOD(ID, 2) = 0
;