-- Q3
SELECT
	title,
	COUNT(*)
FROM
	customer c
		JOIN
	rental r ON c.customer_id = r.customer_id
		JOIN
	inventory i ON r.inventory_id = i.inventory_id
		JOIN
	film f ON i.film_id = f.film_id
WHERE
	first_name = 'GEORGE' AND last_name = 'LINTON'
GROUP BY title
ORDER BY 2 DESC;