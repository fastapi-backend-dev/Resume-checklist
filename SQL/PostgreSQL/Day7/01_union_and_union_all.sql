SELECT first_name AS first_name, 'Actor' AS origin FROM actor
UNION
SELECT first_name, 'Customer' FROM customer
UNION
SELECT UPPER(first_name), 'Staff' FROM staff
ORDER BY 2 DESC;