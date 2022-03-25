/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 보호소에서 중성화한 동물.sql
Purpose : join / like
url     : https://programmers.co.kr/learn/courses/30/lessons/59045?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_INS.ANIMAL_ID
     , ANIMAL_INS.ANIMAL_TYPE
     , ANIMAL_INS.NAME
FROM ANIMAL_INS JOIN ANIMAL_OUTS ON (ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID)
WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE 'Intact%'
     AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%'
        OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY 1
;