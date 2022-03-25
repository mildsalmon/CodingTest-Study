/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 우유와 요거트가 담긴 장바구니.sql
Purpose : 서브 쿼리 / MINUS / JOIN / EXISTS
url     : https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.CART_ID
FROM CART_PRODUCTS A
WHERE NAME = 'Milk'
    AND EXISTS (
        SELECT 1
        FROM CART_PRODUCTS B
        WHERE A.CART_ID = B.CART_ID
            AND B.NAME = 'Yogurt'
    )
;