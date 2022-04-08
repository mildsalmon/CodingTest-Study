/*
Date    : 2022.04.08
Update  : 2022.04.08
Source  : The PADS.sql
Purpose : SELECT / CASE WHEN / CONCAT
url     : https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT CONCAT(name, CASE occupation
                        WHEN 'Doctor' THEN '(D)'
                        WHEN 'Actor' THEN '(A)'
                        WHEN 'Singer' THEN '(S)'
                        WHEN 'Professor' THEN '(P)'
                    END
         ) s
FROM occupations
ORDER BY 1 ASC
;
SELECT CONCAT('There are a total of ', COUNT(occupation),' ', LOWER(occupation), 's.') AS s
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation) ASC, occupation ASC

;