 SELECT EMPNO, ENAME, HIREDATE,
    TO_CHAR(NEXT_DAY(ADD_MONTHS(HIREDATE, 3), '������'), 'YYYY-MM-DD') AS R_JOB,
    NVL(COMMM), 'N/A') AS COMM
 FROM EMP;
 