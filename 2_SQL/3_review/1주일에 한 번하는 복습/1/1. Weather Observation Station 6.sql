SELECT city
FROM STATION
WHERE LOWER(SUBSTR(city, 1, 1)) IN ('a','e','i','o','u');