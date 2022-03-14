/*
Date    : 2022.01.26
Update  : 2022.01.26
Source  : Ollivander's Inventory.sql
Purpose : JOIN / 서브쿼리 / 인라인 뷰
url     : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.id,
    B.age,
    A.coin,
    A.power
FROM (
    SELECT w.id AS id,
           w.code AS code,
           w.power AS power,
           ROW_NUMBER() OVER (PARTITION BY w.code,
                                            w.power
                             ORDER BY w.coins_needed ASC,
                                    w.power DESC) AS num,
           w.coins_needed AS coin
    FROM wands w
) A JOIN (
    SELECT code,
            age
    FROM wands_property
    WHERE is_evil = 0
) B ON (A.code = B.code)
WHERE A.num = 1
ORDER BY A.power DESC,
        B.age DESC
;