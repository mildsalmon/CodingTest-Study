/*
Date    : 2022.04.08
Update  : 2022.04.09
Source  : Type of Triangle.sql
Purpose : CASE WHEN
url     : https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT CASE
        WHEN a + b <= c or a + c <= b or b + c <= a THEN 'Not A Triangle'
        WHEN a = b AND b = c THEN 'Equilateral'
        WHEN a = b OR b = c OR c = a THEN 'Isosceles'
        ELSE 'Scalene'
       END
FROM TRIANGLES
;