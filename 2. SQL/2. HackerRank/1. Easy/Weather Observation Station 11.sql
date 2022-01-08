SELECT DISTINCT(city)
FROM STATION
WHERE LOWER(SUBSTR(city, 1, 1)) NOT IN ('a','e','i','o','u')
    OR LOWER(SUBSTR(city, -1)) NOT IN ('a','e','i','o','u');