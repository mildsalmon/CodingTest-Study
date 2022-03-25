/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 우유와 요거트가 담긴 장바구니.sql
Purpose : 서브 쿼리 / MINUS /
url     : https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk'
    AND CART_ID IN (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = 'Yogurt'
    )
;