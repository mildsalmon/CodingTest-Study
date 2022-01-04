/*
Date    : 2022.01.04
Update  : 2022.01.04
Source  : Revising Aggregations - The Sum Function.sql
Purpose : where / sum
url     : https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT SUM(population)
FROM city
WHERE district = 'California';