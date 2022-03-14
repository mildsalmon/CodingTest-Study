/*
Date    : 2022.01.13
Update  : 2022.01.13
Source  : Weather Observation Station 17.sql
Purpose : ROUND / 서브쿼리
url     : https://www.hackerrank.com/challenges/weather-observation-station-17/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n = (SELECT MIN(sub.lat_n)
              FROM station sub
              WHERE sub.lat_n > 38.7780)
;