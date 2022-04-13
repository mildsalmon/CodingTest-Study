/*
Date    : 2022.04.13
Update  : 2022.04.13
Source  : Binary Tree Nodes.sql
Purpose : CASE WHEN / LEFT JOIN / DISTINCT
url     : https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/
SELECT N
     , CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N NOT IN (SELECT P
                       FROM BST
                       WHERE P IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
       END
FROM BST
ORDER BY 1
;