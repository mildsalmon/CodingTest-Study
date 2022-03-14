/*
Date    : 2022.01.03
Update  : 2022.03.14
Source  : Binary Tree Nodes.sql
Purpose : 계층형 질의 / start with / connect by / connect_by_isleaf / level
url     : https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
*/

SELECT N,
    CASE
        WHEN LEVEL = 1 THEN 'Root'
        WHEN CONNECT_BY_ISLEAF = 1 THEN 'Leaf'
        ELSE 'Inner'
    END
FROM bst
START WITH P IS NULL
CONNECT BY PRIOR N = P
ORDER BY N ASC
;