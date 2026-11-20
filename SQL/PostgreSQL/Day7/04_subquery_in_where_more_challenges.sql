-- Challenge 1
SELECT first_name, last_name
FROM customer
WHERE customer_id IN
(SELECT customer_id
FROM payment
WHERE CAST(payment_date AS date) = '2020-01-25');


-- Challenge 2
SELECT first_name, email
FROM customer
WHERE customer_id IN
(SELECT customer_id FROM payment GROUP BY customer_id HAVING SUM(amount) > 30);


-- Challenge 3
SELECT first_name, last_name, district
FROM customer c JOIN address a ON c.address_id = a.address_id AND district = 'California'
WHERE customer_id IN
(SELECT customer_id FROM payment GROUP BY customer_id HAVING SUM(amount) > 100)
ORDER BY first_name;