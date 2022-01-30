/*
Date    : 2022.01.30
Update  : 2022.01.30
Source  : Ollivander's Inventory.sql
Purpose : JOIN / 인라인뷰/ 서브쿼리 /
url     : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT wands.id,
    non_evil_wands.age,
    wands.coins_needed,
    wands.power
FROM (
    SELECT code, age
    FROM wands_property
    WHERE is_evil = 0
) non_evil_wands
LEFT OUTER JOIN wands
ON (non_evil_wands.code = wands.code)
WHERE (wands.code, wands.power, wands.coins_needed) IN (
    SELECT code,
        power,
        MIN(coins_needed)
    FROM wands
    GROUP BY code, power
)
ORDER BY wands.power DESC, non_evil_wands.age DESC
;