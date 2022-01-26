/*
Date    : 2022.01.26
Update  : 2022.01.26
Source  : Ollivander's Inventory.sql
Purpose : JOIN / 서브쿼리 / 인라인 뷰
url     : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT wands.id,
    wands_p.age,
    wands.coins_needed,
    wands.power
FROM wands
    JOIN (
        SELECT code, age
        FROM wands_property
        WHERE is_evil = 0
    ) wands_p
        ON (wands.code = wands_p.code)
WHERE (wands.coins_needed, wands.code, wands.power) IN (
                        SELECT MIN(coins_needed) AS coin,
                            wands.code,
                            wands.power
                        FROM wands
                        GROUP BY code, power
                    )
ORDER BY wands.power DESC,
    wands_p.age DESC
;