/*
Date    : 2022.01.10
Update  : 2022.01.10
Source  : Revising Aggregations - Averages.sql
Purpose : where / avg
url     : https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT AVG(population)
FROM CITY
WHERE district = 'California';