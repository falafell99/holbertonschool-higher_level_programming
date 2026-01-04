# SQL More Queries

## Description
This directory contains advanced SQL queries and user management exercises. The projects cover MySQL user management, privileges, and more complex SQL operations.

## Projects

### 0. My privileges!
**File:** `0-privileges.sql`

Lists all privileges of MySQL users user_0d_1 and user_0d_2 on localhost.

**Usage:**
```bash
mysql -uroot -p < 0-privileges.sql
1. Root user

File: 1-create_user.sql

Creates MySQL user user_0d_1 with all privileges and sets password.

Usage:

bash
mysql -uroot -p < 1-create_user.sql
SQL Concepts Covered

User Management

CREATE USER: Create new database users
GRANT: Assign privileges to users
SHOW GRANTS: Display user privileges
User authentication and passwords
Privilege Management

Database privileges (SELECT, INSERT, UPDATE, DELETE, etc.)
Administrative privileges
Granting and revoking permissions
Requirements

MySQL 8.0+
Ubuntu 22.04 LTS
Root access to MySQL server
File Structure Convention

All SQL files should have .sql extension
SQL keywords in UPPERCASE
Comments before SQL statements using --
Each file should start with a comment describing the task
Example:

sql
-- Create user with all privileges
CREATE USER IF NOT EXISTS 'username'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
Author

Rafael

License

This project is part of the Holberton School curriculum.
