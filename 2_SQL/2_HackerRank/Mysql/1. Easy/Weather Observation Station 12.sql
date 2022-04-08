/*
Date    : 2022.04.08
Update  : 2022.04.08
Source  : Weather Observation Station 12.sql
Purpose : SELECT / DISTINCT / SUBSTR / NOT IN
url     : https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTR(CITY, 1, 1) NOT IN ('a','e','i','o','u')
    AND SUBSTR(CITY, -1, 1) NOT IN ('a','e','i','o','u')
;