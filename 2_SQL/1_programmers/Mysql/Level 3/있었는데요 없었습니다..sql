/*
Date    : 2022.03.23
Update  : 2022.03.23
Source  : 있었는데요 없었습니다.sql
Purpose : JOIN / INNER JOIN / DATE 대소비교
url     : https://programmers.co.kr/learn/courses/30/lessons/59043?language=mysql
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT I.ANIMAL_ID
     , I.NAME
FROM ANIMAL_INS I JOIN ANIMAL_OUTS O ON (I.ANIMAL_ID = O.ANIMAL_ID)
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME
;