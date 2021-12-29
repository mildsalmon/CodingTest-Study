/*
Date    : 2021.12.29
Update  : 2021.12.29
Source  : Occupations.sql
Purpose : partition by를 사용한 pivot
url     : https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT Doctor, Professor, Singer, Actor
FROM (
    SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS A, name, occupation
    FROM OCCUPATIONS
)
PIVOT
(
    MAX(name)
    FOR occupation IN ('Doctor' AS Doctor,
                       'Professor' AS Professor,
                       'Singer' AS Singer,
                       'Actor' AS Actor)
)
ORDER BY A ASC;