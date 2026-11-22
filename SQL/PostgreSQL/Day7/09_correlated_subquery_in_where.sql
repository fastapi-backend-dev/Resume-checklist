-- Correlated subquery in where

-- Show only those payments that have the highest amount per customer
SELECT *
FROM payment p1
WHERE amount =
(SELECT MAX(amount) FROM payment p2
WHERE p1.customer_id = p2.customer_id)
ORDER BY p1.customer_id;