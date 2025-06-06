-- Query to count the number of author born before 1900 and the number of books they have written
SELECT COUNT(b.book_id) AS book_count, COUNT(DISTINCT a.author_id) AS author_count
FROM authors a
INNER JOIN books b ON a.author_id = b.author_id
WHERE a.birth_year < 1900;

