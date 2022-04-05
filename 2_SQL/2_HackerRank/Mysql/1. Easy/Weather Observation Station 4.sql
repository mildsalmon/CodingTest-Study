/*
Date    : 2022.04.05
Update  : 2022.04.05
Source  : Weather Observation Station 4.sql
Purpose : SELECT / COUNT / DISTINCT
url     : https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT COUNT(city) - COUNT(DISTINCT(city))
FROM station
;