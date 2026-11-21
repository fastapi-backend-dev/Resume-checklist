SELECT *, (SELECT MAX(amount) AS difference FROM payment) - amount AS difference
FROM payment;