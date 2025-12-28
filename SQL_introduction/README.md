# SQL Introduction

## Description
This directory contains introductory SQL exercises and projects. The exercises cover fundamental SQL concepts including database creation, table manipulation, and basic queries.

## Projects

### 0. List databases
**File:** `0-list_databases.sql`

Lists all databases available on the MySQL server.

**Usage:**
```bash
mysql -uroot -p < 0-list_databases.sql
Expected output:

text
Database
information_schema
mysql
performance_schema
sys
SQL Concepts Covered

Database Management

SHOW DATABASES: List all available databases
CREATE DATABASE: Create a new database
DROP DATABASE: Delete a database
Table Operations

CREATE TABLE: Create tables with columns and data types
ALTER TABLE: Modify table structure
DROP TABLE: Delete tables
Data Manipulation

SELECT: Retrieve data from tables
INSERT: Add new records
UPDATE: Modify existing records
DELETE: Remove records
Query Techniques

WHERE: Filter results based on conditions
ORDER BY: Sort results
LIMIT: Restrict number of results
DISTINCT: Get unique values
Requirements

MySQL 8.0+
Ubuntu 22.04 LTS
Basic command-line knowledge
Installation & Setup

1. Start MySQL Server

bash
service mysql start
2. Connect to MySQL

bash
mysql -uroot -p
3. Run SQL Scripts

bash
# Method 1: Pipe input
cat script.sql | mysql -uroot -p

# Method 2: Redirect input
mysql -uroot -p < script.sql

# Method 3: Inside MySQL CLI
mysql> source script.sql
Common MySQL Commands

System Commands

sql
SHOW DATABASES;                    -- List all databases
USE database_name;                 -- Switch to a database
SHOW TABLES;                       -- List tables in current database
DESCRIBE table_name;               -- Show table structure
Database Creation

sql
CREATE DATABASE database_name;     -- Create new database
DROP DATABASE database_name;       -- Delete database
File Structure Convention

All SQL files should have .sql extension
SQL keywords should be in UPPERCASE
Each file should start with a comment describing the task
Comments should be placed before SQL statements using --
Example:

sql
-- List all databases
SHOW DATABASES;
Author

[Your Name]

License

This project is part of the Holberton School curriculum.
