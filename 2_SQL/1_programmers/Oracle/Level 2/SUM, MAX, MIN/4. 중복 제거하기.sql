-- Oracle

SELECT COUNT(NAME)
FROM(
    SELECT NAME
    FROM ANIMAL_INS
    GROUP BY NAME
);

SELECT COUNT(DISTINCT(NAME))
FROM ANIMAL_INS;