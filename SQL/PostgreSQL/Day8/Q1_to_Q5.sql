-- Question 1:
-- Level: Simple
-- Topic: DISTINCT
-- Task: Create a list of all the different (distinct) replacement costs of the films.
-- Question: What's the lowest replacement cost?
-- Answer: 9.99
SELECT
	DISTINCT replacement_cost
FROM
	film
ORDER BY replacement_cost;




-- Question 2:
-- Level: Moderate
-- Topic: CASE + GROUP BY
-- Task: Write a query that gives an overview of how many films have replacements costs in the following cost ranges
-- low: 9.99 - 19.99
-- medium: 20.00 - 24.99
-- high: 25.00 - 29.99
-- Question: How many films have a replacement cost in the "low" group?
-- Answer: 514
SELECT
	-- replacement_cost,
	CASE
		WHEN replacement_cost BETWEEN 9.99 AND 19.99 THEN 'low'
		WHEN replacement_cost BETWEEN 20.00 AND 24.99 THEN 'medium'
		WHEN replacement_cost BETWEEN 25.00 AND 29.99 THEN 'high'
	END AS cost_range,
	COUNT(*)
FROM
	film
GROUP BY
	-- replacement_cost, 
	cost_range;



-- Question 3:
-- Level: Moderate
-- Topic: JOIN
-- Task: Create a list of the film titles including their title, length, and category name ordered descendingly by length.
-- Filter the results to only the movies in the category 'Drama' or 'Sports'.
-- Question: In which category is the longest film and how long is it?
-- Answer: Sports and 184
SELECT
	title,
	length,
	name
FROM
	film f
		JOIN
	film_category fc ON f.film_id = fc.film_id
		JOIN
	category c ON fc.category_id = c.category_id
WHERE name IN ('Drama', 'Sports')
ORDER BY length DESC;



-- Question 4:
-- Level: Moderate
-- Topic: JOIN & GROUP BY
-- Task: Create an overview of how many movies (titles) there are in each category (name).
-- Question: Which category (name) is the most common among the films?
-- Answer: Sports with 74 titles
SELECT
	name, COUNT(*)
FROM
	film f
		JOIN
	film_category fc ON f.film_id = fc.film_id
		JOIN
	category c ON fc.category_id = c.category_id
GROUP BY name
ORDER BY COUNT(*) DESC;




-- Question 5:
-- Level: Moderate
-- Topic: JOIN & GROUP BY
-- Task: Create an overview of the actors' first and last names and in how many movies they appear in.
-- Question: Which actor is part of most movies??
-- Answer: Susan Davis with 54 movies
SELECT
	first_name, last_name, COUNT(*)
FROM
	actor a
		JOIN
	film_actor fa ON a.actor_id = fa.actor_id
		JOIN
	film f ON fa.film_id = f.film_id
GROUP BY first_name, last_name
ORDER BY COUNT(*) DESC;
