-- Query to select each author and their birth year, ordered by birth year in descending order
-- This query retrieves the names of authors and their birth years, sorted by birth year from newest to oldest.
SELECT a.name AS author_name, birth_year    
FROM authors a
ORDER BY birth_year DESC;

