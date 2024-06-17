# https://leetcode.com/problems/game-play-analysis-iv/description/

SELECT 
    ROUND(SUM(temp)/COUNT(DISTINCT player_id), 2) AS fraction
FROM (
    SELECT
        player_id, 
        DATEDIFF(event_date, min(event_date) OVER(PARTITION BY player_id)) = 1 as temp
    FROM
        Activity
) AS t;