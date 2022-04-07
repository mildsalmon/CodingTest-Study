/*
Date    : 2022.04.07
Update  : 2022.04.07
Source  : Weather Observation Station 11.sql
Purpose : SELECT / DISTINCT / SUBSTR / NOT IN
url     : https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT DISTINCT(CITY)
FROM station
WHERE SUBSTR(CITY, 1, 1) NOT IN ('a','e','i','o','u')
    OR SUBSTR(CITY, -1, 1) NOT IN ('a','e','i','o','u')
;
