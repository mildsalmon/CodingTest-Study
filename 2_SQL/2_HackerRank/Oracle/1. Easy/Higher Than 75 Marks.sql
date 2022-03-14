SELECT A.name
FROM (SELECT name
        FROM STUDENTS
        WHERE marks > 75
      ORDER BY SUBSTR(name, -3) ASC, id ASC
      ) A
;
