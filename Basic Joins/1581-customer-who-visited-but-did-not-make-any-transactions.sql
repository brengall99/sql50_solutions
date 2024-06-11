SELECT
    v.customer_id,
    DISTINCT t.visit_id AS count_no_trans
FROM
    Visits v  
LEFT JOIN Transactions t ON v.visit_id = t.visit_id