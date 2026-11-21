SELECT *, (SELECT amount FROM payment LIMIT 1)
FROM payment;