# NoSQL (MongoDB)

## Description
This directory contains MongoDB and NoSQL related exercises. The projects cover MongoDB basics, CRUD operations, aggregations, and working with MongoDB from Python.

## Projects

### 0. List all databases
**File:** `0-list_databases`

Lists all databases in MongoDB using mongo shell command.

**Usage:**
```bash
cat 0-list_databases | mongo
# or
mongo < 0-list_databases
MongoDB Concepts Covered

Basics

NoSQL vs SQL databases
Document-oriented storage (JSON/BSON)
Collections and documents
MongoDB shell commands
CRUD Operations

Create: insertOne(), insertMany()
Read: find(), findOne(), query operators
Update: updateOne(), updateMany()
Delete: deleteOne(), deleteMany()
Advanced Operations

Aggregation pipelines
Indexes and performance
Data modeling in MongoDB
Python with MongoDB

PyMongo library
Connecting to MongoDB from Python
Executing queries and operations
Requirements

MongoDB 4.4+
Ubuntu 20.04 LTS / 22.04 LTS
Python 3.9+ with PyMongo 4.8.0+
Installation

MongoDB 4.4 on Ubuntu 22.04:

bash
# Install dependencies
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install -y libssl1.1

# Add MongoDB repository
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Install MongoDB
sudo apt update
sudo apt install -y mongodb-org

# Start MongoDB
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &
File Structure Convention

MongoDB shell files: plain text with .js or no extension
First line: comment // my comment
Python files: .py extension with shebang #!/usr/bin/env python3
All files end with new line
README.md in each directory
Author

Rafael

License

This project is part of the Holberton School curriculum.
