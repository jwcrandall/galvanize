/*
Implementing queries from
Introduction to SQL for Data Scientists
*/

-- Look at the tables and data shown in Section 1.2

/*
Question 0: Uncomment the query below to run it.
It should give the results of the first query
in Section 2 of the paper.
*/

/*
SELECT
  s.id AS id,
  s.name AS name
FROM
  student AS s
WHERE
  s.id = 1;
*/


/*
Question 1: Write a query that will return the
students whose first name starts with an H.
*/

-- SELECT
--   s.id AS id,
--   s.name AS name
-- FROM
--   student AS s
-- WHERE
--   s.name LIKE 'H%';

-- Back to lecture

/*
Question 2: Write a query that returns what terms degrees were
awarded.
*/
-- SELECT DISTINCT
--   d.term AS term
-- FROM
--   degrees AS d;
--
-- /*
-- Question 3: Write a query that counts the number of times a term
-- g.p.a. was above 3.
-- */
--
-- /* Method 1: */
-- SELECT
--   COUNT(*) AS good_pgas
-- FROM
--   term_gpa AS t
-- WHERE
--   t.gpa > 3;
--
-- /* Method 2: this method is more memory intensive */
-- SELECT
--   SUM(CASE WHEN t.gpa > 3 THEN 1 ELSE 0 END)
-- FROM
--   term_gpa as t;
-- /* Method 3: returns wrong answer */
-- SELECT
--   COUNT(t.gpa > 3) AS good_pgas
-- FROM
--   term_gpa AS t;


-- Back to lecture

/*
Question 4: Uncomment and run this query that uses a join to
duplicate the second set of results in Section 2 of the paper.
*/


SELECT
    s.id AS id,
    s.name AS name,
    t.gpa AS gpa
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
WHERE
    s.id = 1
    AND
    t.term = 2012;



/*
Question 5: Write a query that will find and display Edith Warton's
and Henry James's gpas for 2011 and 2012.
*/


SELECT
    s.id AS id,
    s.name AS name,
    t.gpa AS gpa,
    t.term AS term
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
WHERE
    (s.id = 1 OR s.id = 4)
    AND
    (t.term = 2012 OR t.term = 2011);

/* Question 6: Write a query that will find Edith Warton's and Henry
James's highest gpas rounded to two decimal places.  Order them by
whoever has the highest gpa.
*/

-- SELECT
--     s.name AS name,
--     ROUND(MAX(t.gpa), 2) AS max_GPA
-- FROM
--     student AS s
-- JOIN
--     term_gpa AS t
-- ON
--     s.id = t.id
-- WHERE
--   s.name IN ('Edith Warton', 'Henry James')
-- GROUP BY
--   s.name
-- ORDER BY
--   max_GPA DESC;

-- Back to lecture

/*
Question 7.  In one table list all the students, the term they were
enrolled, their gpa for that term, and the degree they received
(if they received one).  Consider using a left join here.
*/

SELECT
  s.name AS name,
  t.term AS term,
  t.gpa AS gpa,
  d.degree AS degree
FROM
  student AS s
JOIN
  term_gpa AS t
ON
  s.id = t.id
LEFT JOIN
  degrees AS d
ON
  d.id = s.id
  AND
  d.term = t.term;

/*
Query 8: Find the students who have graduated (they have their
degree). Consider using GROUP BY.
*/
/* Method 1: slower method */
SELECT
  s.name AS name
FROM
  student AS s
JOIN
  degrees AS d
ON
  s.id = d.id
GROUP BY
  s.name;

/* Method 2: faster method */
SELECT DISTINCT
  s.name AS name
FROM
  student AS s
JOIN
  degrees AS d
ON
  s.id = d.id;

/*
Query 9:  Find the students who haven't graduated and their average
gpa, rounded to two decimal places. You may want to use a subquery.
*/

SELECT
  s.name AS name,
  ROUND(avg(t.gpa), 2) AS avg_gpa
FROM
  student AS s
JOIN
  term_gpa AS t
ON
  s.id = t.id
GROUP BY
  s.name
HAVING s.name NOT IN (
  SELECT
    s.name AS name
    FROM
      student AS s
    JOIN
      degrees as d
    ON
      s.id = d.id
    GROUP BY
      s.name);












-- Back to lecture
