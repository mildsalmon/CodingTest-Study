/*
Date    : 2022.01.26
Update  : 2022.01.26
Source  : Ollivander's Inventory.sql
Purpose : JOIN / 서브쿼리 / 인라인 뷰
url     : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

WITH
DISTINCT_WAND AS (
    SELECT A.id,
           A.code,
           A.coins_needed,
           A.power
    FROM WANDS A
    WHERE (A.code,
           A.power,
           A.coins_needed) IN (
        SELECT DISTINCT(B.code),
                        B.power,
                        MIN(B.coins_needed)
        FROM WANDS B
        GROUP BY B.code, B.power
        )
),
NON_EVIL_WANDS AS (
    SELECT code,
           age
    FROM WANDS_PROPERTY
    WHERE is_evil = 0
)

SELECT D_W.id,
       N_E_W.age,
       D_W.coins_needed,
       D_W.power
FROM DISTINCT_WAND D_W
    JOIN NON_EVIL_WANDS N_E_W
        ON (D_W.code = N_E_W.code)
ORDER BY D_W.power DESC,
         N_E_W.age DESC
;
