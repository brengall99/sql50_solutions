# https://leetcode.com/problems/exchange-seats/description/

SELECT
    ROW_NUMBER() OVER() id, student
FROM 
    seat
ORDER BY IF(id%2=0, id-1, id+1)