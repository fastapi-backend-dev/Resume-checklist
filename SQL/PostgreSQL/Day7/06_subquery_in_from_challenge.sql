SELECT ROUND(AVG(total_amount), 2) AS avg_daily_amt
FROM
(SELECT DATE(payment_date), SUM(amount) AS total_amount
FROM payment
GROUP BY DATE(payment_date)) AS subquery;