SELECT city
FROM STATION
WHERE LOWER(SUBSTR(city, 1, 1)) IN ('a','e','i','o','u')
    AND LOWER(SUBSTR(city, LENGTH(city))) IN ('a','e','i','o','u');