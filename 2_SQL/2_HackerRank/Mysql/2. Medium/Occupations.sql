/*
Date    : 2022.04.13
Update  : 2022.04.13
Source  : Occupations.sql
Purpose : CASE WHEN / ROW_NUMBER / WINDOW / MAX
url     : https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/
SELECT MAX(CASE WHEN A.occupation = 'Doctor' THEN A.name END)
     , MAX(CASE WHEN A.occupation = 'Professor' THEN A.name END)
     , MAX(CASE WHEN A.occupation = 'Singer' THEN A.name END)
     , MAX(CASE WHEN A.occupation = 'Actor' THEN A.name END)
FROM (
    SELECT name
         , ROW_NUMBER() OVER(PARTITION BY occupation ORDER BY name) AS cnt
         , occupation
    FROM occupations
) A
GROUP BY cnt
ORDER BY cnt
;