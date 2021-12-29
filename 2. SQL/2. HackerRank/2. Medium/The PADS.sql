/*
Date    : 2021.12.29
Update  : 2021.12.29
Source  : Occupations.sql
Purpose : partition by를 사용한 pivot
url     : https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT MAX(DECODE(occupation, 'Doctor', name)) AS Doctor,
        MAX(DECODE(occupation, 'Professor', name)) AS Professor,
        MAX(DECODE(occupation, 'Singer', name)) AS Singer,
        MAX(DECODE(occupation, 'Actor', name)) AS Actor
FROM (
    SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS rank, name, occupation
    FROM OCCUPATIONS
)
GROUP BY rank
ORDER BY rank ASC;
