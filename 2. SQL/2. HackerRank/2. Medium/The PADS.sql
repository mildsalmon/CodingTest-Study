/*
Date    : 2021.12.29
Update  : 2021.12.29
Source  : The PADS.sql
Purpose : name에는 concat / occupation에는 group by를 사용함.
url     : https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.name
FROM (SELECT name || '(' || UPPER(SUBSTR(occupation, 1, 1)) || ')' AS name
      FROM OCCUPATIONS
      ORDER BY name ASC
      ) A
UNION
SELECT B.text
FROM (SELECT 'There are a total of ' || COUNT(occupation) || ' ' || LOWER(occupation) || 's.' AS text
      FROM OCCUPATIONS
      group by occupation
      ORDER BY COUNT(occupation) ASC, occupation ASC
      ) B
;