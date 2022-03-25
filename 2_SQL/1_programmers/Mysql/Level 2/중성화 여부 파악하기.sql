/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 중성화 여부 파악하기.sql
Purpose : LIKE / CASE WHEN
url     : https://programmers.co.kr/learn/courses/30/lessons/59409?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , NAME
     , CASE
        WHEN SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
        ELSE 'X'
       END
FROM ANIMAL_INS
ORDER BY 1
;