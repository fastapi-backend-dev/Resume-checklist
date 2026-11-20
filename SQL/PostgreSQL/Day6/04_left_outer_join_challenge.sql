SELECT
	s.seat_no,
	COUNT(*) AS count_seats
FROM
	seats s
		LEFT JOIN
	boarding_passes bp ON s.seat_no = bp.seat_no
GROUP BY s.seat_no
ORDER BY count_seats DESC;


SELECT
	RIGHT(s.seat_no, 1) as seat_line,
	COUNT(*) AS count_seats
FROM
	seats s
		LEFT JOIN
	boarding_passes bp ON s.seat_no = bp.seat_no
GROUP BY seat_line
ORDER BY count_seats DESC;