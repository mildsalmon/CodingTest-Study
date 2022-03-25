/*
Date    : 2022.03.25
Update  : 2022.03.25
Source  : 루시와 엘라 찾기.sql
Purpose : IN
url     : https://programmers.co.kr/learn/courses/30/lessons/59046?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT ANIMAL_ID
     , NAME
     , SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
;