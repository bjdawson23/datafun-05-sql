-- Query to count the number of books written by each author
SELECT nationality,
       COUNT(b.book_id) AS book_count
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY nationality
ORDER BY nationality ASC;

