SELECT
	EXTRACT(MONTH from rental_date) AS rental_day,
	COUNT(*) AS total_sales
FROM
	rental
GROUP BY rental_day
ORDER BY total_sales DESC;