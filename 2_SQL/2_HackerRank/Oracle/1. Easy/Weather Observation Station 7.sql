SELECT DISTINCT(city)
FROM STATION
WHERE LOWER(SUBSTR(city, LENGTH(city))) IN ('a','e','i','o','u');