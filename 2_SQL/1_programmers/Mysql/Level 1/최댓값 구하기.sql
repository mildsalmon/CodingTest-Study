/*
Date    : 2021.03.21
Update  : 2021.03.21
Source  : 최댓값 구하기.sql
Purpose : 최대값 구하기
url     : https://programmers.co.kr/learn/courses/30/lessons/59415?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
;