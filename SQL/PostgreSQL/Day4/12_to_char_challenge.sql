-- Format 1: Dy, DD/MM/YYYY
SELECT
	SUM(amount),
	TO_CHAR(payment_date, 'Dy, DD/MM/YYYY') AS format1
FROM
	payment
GROUP BY format1
ORDER BY SUM(amount);



-- Format 2: Mon, YYYY
SELECT
	SUM(amount),
	TO_CHAR(payment_date, 'Mon, YYYY') AS format2
FROM
	payment
GROUP BY format2
ORDER BY SUM(amount);




-- Format 3: Dy, HH:MM
SELECT
	SUM(amount),
	TO_CHAR(payment_date, 'Dy, HH:MI') AS format3
FROM
	payment
GROUP BY format3
ORDER BY SUM(amount) DESC;
	