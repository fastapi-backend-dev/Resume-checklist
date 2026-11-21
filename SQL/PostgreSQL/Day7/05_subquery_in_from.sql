SELECT ROUND(AVG(total_amount), 2) AS avg_lifetime_spend
FROM
(SELECT customer_id, SUM(amount) AS total_amount
FROM payment
GROUP BY customer_id) AS subquery;