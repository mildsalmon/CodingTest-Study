/*
Date    : 2022.01.22
Update  : 2022.01.22
Source  : Weather Observation Station 20.sql
Purpose : 중앙값 / MEDIAN / window function / count / row_number / ceil / floor / avg / round
url     : https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ROUND(AVG(lat_n) ,4)
FROM (SELECT lat_n,
        ROW_NUMBER() OVER(ORDER BY lat_n) AS RN,
        COUNT(*) OVER() + 1 AS C
     FROM station)
WHERE RN IN (CEIL(C/2), FLOOR(C/2))
;