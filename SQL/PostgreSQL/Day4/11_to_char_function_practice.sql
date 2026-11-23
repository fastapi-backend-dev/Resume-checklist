-- Syntax
-- TO_CHAR(date/time/interval/number, format)
-- Example1: TO_CHAR(rental_date, 'MM-YYYY')
SELECT
	SUM(amount),
	TO_CHAR(payment_date, 'Dy Month YYYY')
FROM
	payment
GROUP BY
	TO_CHAR(payment_date, 'Dy Month YYYY');