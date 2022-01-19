/*
Date    : 2022.01.01
Update  : 2022.01.01
Source  : Occupations.sql
Purpose :
url     : https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT MAX(CASE WHEN Occupation = 'Doctor' THEN Name END) AS 'Doctor',
        MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS 'Professor',
        MAX(CASE WHEN Occupation = 'Singer' THEN Name END) AS 'Singer',
        MAX(CASE WHEN Occupation = 'Actor' THEN Name END) AS 'Actor'
FROM (SELECT ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY name ASC) AS rank,
            Name, Occupation
    FROM OCCUPATIONS)
GROUP BY rank
ORDER BY rank ASC;