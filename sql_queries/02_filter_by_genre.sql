-- Query to count the number of books written by each author
SELECT genre, COUNT(b.book_id) AS book_count
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id
GROUP BY genre
ORDER BY book_count DESC;


