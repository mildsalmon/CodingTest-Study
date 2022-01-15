/*
Date    : 2022.01.15
Update  : 2022.01.15
Source  : Weather Observation Station 15.sql
Purpose : ROUND / 서브쿼리
url     : https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n = (SELECT MAX(a.lat_n)
              FROM station a
              WHERE a.lat_n < 137.2345)
;