/*
Date    : 2022.03.28
Update  : 2022.03.28
Source  : Revising the Select Query I.sql
Purpose : WHERE
url     : https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ID
     , NAME
     , COUNTRYCODE
     , DISTRICT
     , POPULATION
FROM CITY
WHERE COUNTRYCODE = 'USA'
    AND POPULATION > 100000
;