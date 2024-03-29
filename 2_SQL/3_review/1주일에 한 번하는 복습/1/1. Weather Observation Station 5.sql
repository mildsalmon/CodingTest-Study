SELECT city, LENGTH(city)
FROM (SELECT city
      FROM STATION
      ORDER BY LENGTH(city) ASC, city)
WHERE ROWNUM = 1
UNION
SELECT city, LENGTH(city)
FROM (SELECT city
      FROM STATION
      ORDER BY LENGTH(city) DESC, city)
WHERE ROWNUM = 1
ORDER BY city ASC;
