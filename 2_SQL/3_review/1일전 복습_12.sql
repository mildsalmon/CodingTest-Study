-- 루시와 엘라 찾기

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE UPPER(NAME) IN (UPPER('LUCY'),
                      UPPER('ELLA'),
                      UPPER('PICKLE'),
                      UPPER('ROGAN'),
                      UPPER('SABRINA'),
                      UPPER('MITTY'))
ORDER BY ANIMAL_ID ASC;

-- 이름에 el이 들어가는 동물 찾기

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'
    AND UPPER(NAME) LIKE '%EL%'
ORDER BY NAME ASC;

-- NULL 처리하기

SELECT ANIMAL_TYPE,
    NVL(NAME, 'No name'),
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;