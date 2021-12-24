SELECT city, LENGTH(city)
FROM (SELECT city
     FROM STATION
     ORDER BY city ASC, LENGTH(city)
      )
WHERE ROWNUM = 1
UNION
SELECT city, LENGTH(city)
FROM (SELECT city
      FROM STATION
      ORDER BY city DESC, LENGTH(city)
      )
WHERE ROWNUM = 1;
