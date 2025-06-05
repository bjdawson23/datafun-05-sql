# datafun-05-sql
datafun-05-sql  Summer 1 - Module 5 SQL Project

## 1. Virtual Environment Management (Windows PowerShell)

1. **Create a virtual environment**
   ```powershell
   py -m venv .venv
   ```

2. **Activate the virtual environment**
   ```powershell
   .\.venv\Scripts\activate
   ```

3. **Upgrade pip, setuptools, and wheel**
   ```powershell
   py -m pip install --upgrade pip setuptools wheel
   ```

4. **Install required packages**
   ```powershell
   py -m pip install --upgrade -r requirements.txt
   ```

---

## 2. Running Python Scripts

- Activate your `.venv` and ensure all required packages are installed.
- Verify all external packages in your scripts are listed in `requirements.txt`.

**Run Python scripts:**
```powershell
py demo_script.py
py do_stats.py
py draw_chart.py
py greet_user.py
```

---

## 3. Repeatable Workflow Checklist

When resuming work on your project, follow these steps:

1. [Pull latest changes](https://github.com/denisecase/pro-analytics-01/tree/main/03-repeatable-workflow)
2. Activate virtual environment
3. Install dependencies
4. Run Python scripts
5. Modify and test code
6. Add, commit, and push changes to Git

---

## 4. Git Add-Commit-Push CheatSheet

```powershell
git clone https://github.com/youraccount/yourrepo
git add .
git commit -m "custom message"
git push -u origin main
git pull origin main
git push
```

---

## P5 SQL

Step 1: Start Project, Open in VS Code

  1. created data forlder for csv files
  2. added example scripts and sql folders

Step 2: Add/Update Critical Files

    The .gitignore file tells Git files to ignore when committing changes.
    Review/copy the example .gitignore file, you might be able to use it without modification.

    The requirements.txt file lists the packages used in the project.

git add .
git commit -m "Add .gitignore and requirements.txt"
git push -u origin main

Step 3: Set up Virtual Environment

A. Create .venv B. Activate .venv C. Install dependencies into .venv D. Select VS Code interpreter to use .venv

Step 4: Schema Design and Database Initialization

Design a schema with at least two related tables, including foreign key constraints. 
schema design authors:
    author_id TEXT PRIMARY KEY, -- Prefixed sequential ID as the primary key (e.g., AUTHOR_001)
    name TEXT NOT NULL,         -- Author's name (mandatory field)
    birth_year INTEGER,         -- Year of birth (optional)
    nationality TEXT            -- Nationality of the author (optional)

schema design books:
    book_id TEXT PRIMARY KEY,   -- Prefixed sequential ID as the primary key (e.g., BOOK_001)
    title TEXT NOT NULL,        -- Book title (mandatory field)
    genre TEXT,                 -- Book genre (optional)
    publication_year INTEGER,   -- Year of publication (optional)
    author_id TEXT,             -- Foreign key linking to authors
    author_age_at_publication INT, -- Age of Author at Publication Year (calculated: publication_year - birth_year)
    FOREIGN KEY (author_id) REFERENCES authors (author_id) -- Relationship with authors

sql_create folder:

    01_drop_tables.sql - drop tables to restart
    02_create_tables.sql - create your database schema using sql
    03_insert_records.sql - insert at least 10 additional records into each table.

db01_setup.py:

Create a Python script that demonstrates the ability to create a database, define a schema, and insert records. Make it easy to re-run by dropping the tables first.

Step 5. Cleaning and Feature Engineering

Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements. 

sql_features folder:

    update_records.sql - update 1 or more records in a table.
    delete_records.sql - delete 1 or more records from a table.

db02_features.py

Create a Python script that demonstrates the ability to run sql scripts to interact with fields, update records, delete records, and maybe add additional columns.

Step 6. Perform Aggregations and queries

Implement SQL statements and queries to perform aggregations and queries.

sql_queries folder:

    query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
    query_filter.sql - use WHERE to filter data based on conditions.
    query_sorting.sql - use ORDER BY to sort data.
    query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
    query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings:

db03_queries.py
