-- Challenge 1
SELECT
	EXTRACT(MONTH FROM payment_date) AS payment_month,
	SUM(amount) AS total_payment_amount
FROM
	payment
GROUP BY payment_month
ORDER BY total_payment_amount DESC;


-- Challenge 2
SELECT
	EXTRACT(DOW FROM payment_date) AS day_of_week,
	SUM(amount) AS total_payment_amount
FROM
	payment
GROUP BY day_of_week
ORDER BY total_payment_amount DESC;



-- Challenge 3
SELECT
	EXTRACT(WEEK FROM payment_date) AS week_num,
	customer_id,
	SUM(amount) AS total_payment_amount
FROM
	payment
GROUP BY week_num, customer_id
ORDER BY total_payment_amount DESC;