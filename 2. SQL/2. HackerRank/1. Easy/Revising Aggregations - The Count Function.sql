/*
Date    : 2022.01.04
Update  : 2022.01.04
Source  : Revising Aggregations - The Count Function.sql
Purpose : where / count
url     : https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT COUNT(id)
FROM city
WHERE population > 100000;