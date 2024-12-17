# https://leetcode.com/problems/product-sales-analysis-i/description/

SELECT
    p.product_name,
    s.year,
    s.price
FROM
    Product p
LEFT JOIN
    Sales s
ON
    p.product_id = s.product_id
WHERE
    price IS NOT NULL;