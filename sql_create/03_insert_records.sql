-- Insert records into the authors table first
INSERT INTO authors (author_id, name, birth_year, nationality) VALUES
    ('AUTHOR_001', 'J.K. Rowling', 1965, 'British'),
    ('AUTHOR_002', 'George Orwell', 1903, 'British'),
    ('AUTHOR_003', 'Jane Austen', 1775, 'English'),    
    ('AUTHOR_004', 'Charles Dickens', 1812, 'English'),
    ('AUTHOR_005', 'Dr. Seuss', 1904, 'American'),    
    ('AUTHOR_006', 'Harper Lee', 1926, 'American'),
    ('AUTHOR_007', 'David McCullough', 1933, 'American'),
    ('AUTHOR_008', 'Mark Kurlansky', 1948, 'American'),
    ('AUTHOR_009', 'F. Scott Fitzgerald', 1896, 'American'),
    ('AUTHOR_010', 'James Joyce', 1882, 'Irish'),
    ('AUTHOR_011', 'J.R.R Tolkien', 1892, 'English'),
    ('AUTHOR_012', 'J. D. Salinger', 1919, 'American'),
    ('AUTHOR_013', 'Herman Melville', 1819, 'American');

-- Insert records into the books table
-- And include foreign key references to the authors table
-- IMPORTANT: No tic marks inside a string, use two single quotes to escape a single quote
INSERT INTO books (book_id, title, genre, publication_year, author_id) VALUES
    ('BOOK_001', 'Harry Potter and the Sorcerer''s Stone', 'Fantasy', 1997, 'AUTHOR_001'),
    ('BOOK_002', 'Harry Potter and the Chamber of Secrets', 'Fantasy', 1998, 'AUTHOR_001'),
    ('BOOK_003', '1984', 'Dystopian', 1949, 'AUTHOR_002'),
    ('BOOK_004', 'Animal Farm', 'Political Satire', 1945, 'AUTHOR_002'),
    ('BOOK_005', 'Pride & Prejudice', 'Romance Novel', 1813, 'AUTHOR_003'),
    ('BOOK_006', 'The Cat in the Hat', 'Childrens Literature', 1957, 'AUTHOR_005'),
    ('BOOK_007', 'A Christmas Carol', 'Christmas Tale', 1843, 'AUTHOR_004'),
    ('BOOK_008', 'To Kill a Mockingbird', 'Fiction', 1960, 'AUTHOR_006'),
    ('BOOK_009', '1776', 'History', 2005, 'AUTHOR_007'),
    ('BOOK_010', '1968: The Year that Rocked the World ', 'History', 2003, 'AUTHOR_008'),
    ('BOOK_011', 'The Great Gatsby', 'Fiction', 1925, 'AUTHOR_009'),
    ('BOOK_012', 'Ulysses', 'Fiction', 1922, 'AUTHOR_010'),
    ('BOOK_013', 'The Lord of the Rings', 'Fiction', 1954, 'AUTHOR_011'),
    ('BOOK_014', 'The Catcher in the Rye', 'Fiction', 1951, 'AUTHOR_012'),
    ('BOOK_015', 'Moby-Dick', 'Fiction', 1851, 'AUTHOR_013'),
    ('BOOK_016', 'John Adams', 'History', 1960, 'AUTHOR_007');
 