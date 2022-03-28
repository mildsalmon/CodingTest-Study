/*
Date    : 2022.03.28
Update  : 2022.03.28
Source  : Revising the Select Query II.sql
Purpose : WHERE
url     : https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT NAME
FROM CITY
WHERE population > 120000
    AND countrycode = 'USA'
;