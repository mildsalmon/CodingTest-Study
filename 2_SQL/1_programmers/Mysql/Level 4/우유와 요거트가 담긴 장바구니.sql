/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 우유와 요거트가 담긴 장바구니.sql
Purpose : 서브 쿼리 / MINUS / JOIN
url     : https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT A.CART_ID
FROM CART_PRODUCTS A JOIN CART_PRODUCTS B ON (A.CART_ID = B.CART_ID)
WHERE A.NAME = 'Milk' AND B.NAME = 'Yogurt'
;