/*
Date    : 2021.12.29
Update  : 2021.12.29
Source  : Occupations.sql
Purpose : partition by를 사용한 pivot
url     : https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT MAX(CASE WHEN occupation = 'Doctor' THEN name END) AS Doctor,
        MAX(CASE WHEN occupation = 'Professor' THEN name END) AS Professor,
        MAX(CASE WHEN occupation = 'Singer' THEN name END) AS Singer,
        MAX(CASE WHEN occupation = 'Actor' THEN name END) AS Actor
FROM (
    SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS rank, name, occupation
    FROM OCCUPATIONS
)
GROUP BY rank
ORDER BY rank ASC;