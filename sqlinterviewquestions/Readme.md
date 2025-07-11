# Index
## Basic Level Quesions
1. [What is SQL](#what-is-sql)  
2. [What is difference between SQL and MySQL](#what-is-difference-between-sql-and-mysql) 
3. [What is difference between SQL and NoSQL](#what-is-difference-between-sql-and-nosql)
4. [What are the different types of SQL statements](#what-are-the-different-types-of-sql-statements)  
5. [What are constraints](#what-are-constraints) 
6. [What is difference between Primary key and unique key](#what-is-difference-between-primary-key-and-unique-key)
7. [What is a primary key and foreign key](#what-is-a-primary-key-and-foreign-key)  
8. [What is the difference between DELETE, TRUNCATE, and DROP](#what-is-the-difference-between-delete-truncate-and-drop) 
9. [What are operators,share its type and example](#what-are-operators-share-its-type-and-example)
10. [What is the difference between WHERE and HAVING clause](#what-is-the-difference-between-where-and-having-clause)  
11. [What are Aggregate Functions in SQL](#what-are-aggregate-functions-in-sql)
12. [What is a GROUP BY clause? How is it used with aggregate functions](#what-is-a-group-by-clause-how-is-it-used-with-aggregate-functions)  
13. [What is a subquery, Explain with an example](#what-is-a-subquery-explain-with-an-example) 
14. [What is difference between GROUP BY and ORDER BY](#what-is-difference-between-group-by-and-order-by) 
15. [What are the different types of joins in SQL](#what-are-the-different-types-of-joins-in-sql)   
16. [What is the difference between UNION and UNION ALL](#what-is-the-difference-between-union-and-union-all)  
17. [What is the difference between UNION and JOIN](#what-is-the-difference-between-union-and-join)
18. [What is CASE Statement in SQL](#what-is-case-statement-in-sql)  
19. [How to handle NULL values in SQL](#how-to-handle-null-values-in-sql)   
20. [How to Optimize SQL Queries](#how-to-optimize-sql-queries)  
21. [What is the difference between IN and EXISTS](#what-is-the-difference-between-in-and-exists)
22. [What is normalization and denormalization](#what-is-normalization-and-denormalization) 
23. [What is INDEX](#what-is-index) 
 




## Query Questions

1. [Write a query to find the second highest salary from an Employee table](#write-a-query-to-find-the-second-highest-salary-from-an-employee-table)  



## Intermediate Level  Questions


1. [What are window functions, How do you use RANK(), DENSE_RANK(), ROW_NUMBER()](#what-are-window-functions-how-do-you-use-rank-dense_rank-row_number)  
2. [Explain CTE (Common Table Expression) and its benefits](#explain-cte-common-table-expression-and-its-benefits)  
3. [How do transactions work in SQL? What are ACID properties](#how-do-transactions-work-in-sql-what-are-acid-properties)  
4. [What is the difference between IN and EXISTS](#what-is-the-difference-between-in-and-exists)  
5. [Explain stored procedures, triggers, and views](#explain-stored-procedures-triggers-and-views)
6. [What is the purpose of ALter Command](#what-is-the-purpose-of-alter-command)
7. [What Order of Execution of SQL Clauses](#what-order-of-execution-of-sql-clauses)





## Basic Level Questions

1. ### What is SQL

    **SQL (Structured Query Language)** is a standard language used to communicate with relational databases and perform many different data manipulaton operations on the data. It allows users to **store, retrieve, manipulate, and manage data** efficiently.

    ### ✅ Key Uses of SQL

    1. **Data Retrieval**
    - Query data from single or multiple tables using `SELECT` statements.

    2. **Data Insertion**
    - Insert new records into tables using the `INSERT INTO` statement.

    3. **Data Updating**
    - Modify existing records with the `UPDATE` command.

    4. **Data Deletion**
    - Remove unwanted records using the `DELETE` command.

    5. **Database Creation**
    - Create new databases and tables using `CREATE DATABASE` and `CREATE TABLE`.

    6. **Data Filtering**
    - Apply conditions with `WHERE`, `BETWEEN`, `LIKE`, etc., to filter specific records.

    7. **Data Sorting**
    - Order results using `ORDER BY`.

    8. **Aggregation and Grouping**
    - Use functions like `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` with `GROUP BY` to summarize data.

    9. **Joins**
    - Combine data from multiple tables using `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, etc.

    10. **Constraints & Integrity**
        - Enforce rules like `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL` to ensure data integrity.

    11. **Permissions and Access Control**
        - Manage user access with `GRANT` and `REVOKE` statements.

    12. **Views and Stored Procedures**
        - Create virtual tables (views) and reusable logic (stored procedures) to simplify queries.

    13. **Data Export and Import**
        - Move data between systems using SQL export/import tools.

    ---

    **In summary**, SQL is essential for working with relational databases. It helps analysts, developers, and database administrators manage data effectively and power various applications.



2. ###  what is difference between SQL and MySQL
    Difference between SQL and MySQL
    | SQL (Structured Query Language)                               | MySQL (Database Management System)                         |
    |---------------------------------------------------------------|-------------------------------------------------------------|
    | It is a **query language** used to manage data in RDBMS.      | It is a **software** (RDBMS) that uses SQL to manage data.  |
    | It is a **language standard**, not a tool/software.           | It is an **open-source database system**.                   |
    | Used to **write queries** like `SELECT`, `INSERT`, etc.       | Used to **store, retrieve, and manage** data using SQL.     |
    | SQL is **ISO/ANSI standard** and universal.                   | MySQL is **maintained by Oracle Corporation**.              |
    | Cannot store data by itself.                                  | Actually stores and manages data.                           |
    | Applies to many databases (MySQL, PostgreSQL, Oracle, etc.)   | One specific software that implements SQL.                  |


3. ### What is difference between SQL and NoSQL
    | SQL (Relational Databases)                        | NoSQL (Non-Relational Databases)                            |
    |--------------------------------------------------|-------------------------------------------------------------|
    | Stands for Structured Query Language             | Stands for "Not Only SQL"                                   |
    | Uses **tables** with rows and columns            | Uses **documents**, **key-value**, **graph**, or **wide-column** formats |
    | Schema is **fixed and predefined**               | Schema is **dynamic and flexible**                          |
    | Follows **ACID** properties strictly             | Follows **CAP theorem**, focuses on availability & partition tolerance |
    | Best for structured data with clear relationships| Best for unstructured or semi-structured data               |
    | Examples: MySQL, PostgreSQL, Oracle, SQL Server  | Examples: MongoDB, Cassandra, Redis, CouchDB                |
    | Scales **vertically** (more power to single server) | Scales **horizontally** (add more servers)                |
    | Supports **complex JOINs and transactions**      | Limited JOINs, but great for fast reads/writes              |




4. ### What are the different types of SQL statements
    ### Types of SQL Statements

    SQL statements are categorized based on the type of operation they perform on the database. The main types are:

    

    ### 1. 🧱 Data Definition Language (DDL)
    Used to define and modify the structure of database objects (tables, schemas, etc.).

    - `CREATE` – Creates a new table or database.
    - `ALTER` – Modifies an existing table structure.
    - `DROP` – Deletes a table or database.
    - `TRUNCATE` – Removes all records from a table (faster than DELETE).

   

    ### 2. 📝 Data Manipulation Language (DML)
    Used to manipulate data stored in database tables.

    - `SELECT` – Retrieves data from tables.
    - `INSERT` – Adds new data/records.
    - `UPDATE` – Modifies existing records.
    - `DELETE` – Removes records from a table.

  

    ### 3. 🔐 Data Control Language (DCL)
    Used to control access to data and permissions.

    - `GRANT` – Gives user access privileges.
    - `REVOKE` – Removes user access privileges.

   

    ### 4. 🧪 Transaction Control Language (TCL)
    Used to manage transactions in a database to ensure data integrity.

    - `COMMIT` – Saves all changes made in the current transaction.
    - `ROLLBACK` – Reverts changes back to the last commit.
    - `SAVEPOINT` – Sets a point in a transaction to which you can roll back later.
    - `SET TRANSACTION` – Sets the properties for a transaction.

   

    ### 5. 🧠 Data Query Language (DQL)
    Focused on fetching/querying data from the database.

    - `SELECT` – Used to query and retrieve data.

    > Note: `SELECT` is often grouped under DML but technically forms its own category, DQL.



    ### ✅ Summary

    | Type | Purpose |
    |------|---------|
    | DDL  | Define database structure |
    | DML  | Manage data in tables |
    | DCL  | Manage user permissions |
    | TCL  | Manage transactions |
    | DQL  | Retrieve data |


5. ### What are constraints

#### Constraints are rules applied to table columns to enforce data integrity and consistency.
**Types of constraints**
| Constraint       | Description                                                                |
| ---------------- | -------------------------------------------------------------------------- |
| `PRIMARY KEY`    | Uniquely identifies each row in a table. Cannot be NULL.                   |
| `FOREIGN KEY`    | Enforces a link between two tables based on a referenced column.           |
| `UNIQUE`         | Ensures all values in a column are different.                              |
| `NOT NULL`       | Prevents NULL values in a column.                                          |
| `CHECK`          | Ensures all values in a column satisfy a specific condition.               |
| `DEFAULT`        | Assigns a default value if none is provided.                               |
| `AUTO_INCREMENT` | Automatically generates sequential numeric values (mostly for PK columns). |

#### Examples
1. ##### PRIMARY KEY & NOT NULL
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

```
2. ##### UNIQUE
```sql 
ALTER TABLE students
ADD CONSTRAINT unique_email UNIQUE (email);


```
3. #### FOREIGN KEY
```sql
CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


```

4. #### CHECK
```sql 

CREATE TABLE products (
    price DECIMAL(10,2),
    CHECK (price > 0)
);

```

5.  #### DEFAULT
```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'Active'
);

```

6. #### AUTO_INCREMENT

```sql
CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    issue TEXT
);

```










6. ### What is difference between Primary key and unique key
#### 🔑 Primary Key vs UNIQUE Key (Simplified)

| Primary Key                                        | UNIQUE Key                                         |
|----------------------------------------------------|----------------------------------------------------|
| Uniquely identifies each row in a table            | Ensures all values in the column are unique        |
| ❌ Does not allow NULL values                      | ✅ Allows one NULL value (in most databases)        |
| Only one primary key per table                     | Can have multiple UNIQUE keys                      |
| Creates a unique **clustered index** automatically | Creates a unique **non-clustered index**           |
| Used to uniquely identify a record                 | Used to enforce uniqueness without being the main identifier |


7. ### What is a primary key and foreign key


    ### Primary Key vs Foreign Key in SQL


    ### 🔑 Primary Key

    - A **primary key** is a column (or a set of columns) that **uniquely identifies each row** in a table.
    - It **must be unique** and **cannot be NULL**.
    - Each table can have **only one primary key**.
    - Ensures **data integrity** by preventing duplicate entries.

    ### Example:
    ```sql
    CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name VARCHAR(100)
    );
    ```
    > Here, `student_id` uniquely identifies each student.



    ### 🔗 Foreign Key

    - A **foreign key** is a column in one table that **refers to the primary key** in another table.
    - It is used to **link two tables together**.
    - Maintains **referential integrity** between records.
    - Can contain **duplicate** and **NULL values** depending on the design.

    ### Example:
    ```sql
    CREATE TABLE enrollments (
        enrollment_id INT PRIMARY KEY,
        student_id INT,
        course_id INT,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    ```
    > Here, `student_id` in `enrollments` references `student_id` in `students`.



    ### 📌 Key Differences

    | Feature         | Primary Key                     | Foreign Key                                  |
    |----------------|----------------------------------|----------------------------------------------|
    | Uniqueness      | Must be unique                  | Can have duplicates                          |
    | NULL allowed?   | No                              | Yes (optional)                               |
    | Purpose         | Uniquely identifies each row    | Establishes relationship between tables      |
    | Table count     | One per table (only one PK)     | Can have multiple FKs in a table             |



    ### ✅ Summary

    - Use a **primary key** to uniquely identify each row in a table.
    - Use a **foreign key** to establish relationships between tables and maintain consistency.


8. ### What is the difference between DELETE, TRUNCATE, and DROP

    ### 🧨 Difference Between DELETE, TRUNCATE, and DROP

    | Feature              | DELETE | TRUNCATE | DROP |
    |----------------------|--------|----------|------|
    | **Purpose**          | The `DELETE` statement is used to remove specific rows from a table based on a condition. | The `TRUNCATE` statement removes **all rows** from a table without logging individual row deletions. | The `DROP` statement completely removes the table from the database, including its structure and data. |
    | **Can use WHERE?**   | Yes, you can use a `WHERE` clause to specify which rows to delete. | No, `TRUNCATE` removes all rows; it does not support a `WHERE` clause. | No, `DROP` removes the entire table; it cannot filter rows. |
    | **Transaction Safe?**| The `DELETE` command is transaction-safe; it can be rolled back if used within a transaction. | `TRUNCATE` can be rolled back in some databases (e.g., PostgreSQL) but **not in all** (e.g., MySQL without InnoDB). | The `DROP` statement **cannot be rolled back** once executed, and the table is lost. |
    | **Performance**      | `DELETE` is generally slower because it logs each deleted row and fires any associated triggers. | `TRUNCATE` is faster than `DELETE` because it deallocates data pages instead of row-by-row deletion. | `DROP` is the fastest, as it removes the entire table in one action. |
    | **Triggers**         | Yes, `DELETE` will activate any `DELETE` triggers on the table. | No, `TRUNCATE` does not fire `DELETE` triggers. | No, `DROP` does not activate any triggers. |
    | **Identity Reset?**  | No, the identity column (like auto-increment ID) is **not reset** after a `DELETE`. | Yes, in most databases, the identity counter is **reset to its seed value** after `TRUNCATE`. | Yes, since the table is removed entirely, any identity values are also lost. |
    | **Locks Used**       | `DELETE` uses **row-level locks**, especially with conditions. | `TRUNCATE` typically uses a **table-level lock**. | `DROP` locks the table completely as it is being removed. |
    | **Use Case**         | Use when you want to delete specific rows from a table. | Use when you want to quickly remove all data but keep the table structure. | Use when you no longer need the table or want to recreate it from scratch. |

    ---

    ### 🔹 DELETE Example
    ```sql
    DELETE FROM employees WHERE department = 'HR';
    ```
    ➡️ This deletes only the employees who belong to the HR department.

    ---

    ### 🔹 TRUNCATE Example
    ```sql
    TRUNCATE TABLE employees;
    ```
    ➡️ This quickly removes **all rows** from the `employees` table without logging each deletion.

    ---

    ### 🔹 DROP Example
    ```sql
    DROP TABLE employees;
    ```
    ➡️ This completely **removes the `employees` table**, including its structure and all data.


9. ### What are operators, share its type and example
    ### ✅ SQL Operators

    SQL operators are used to perform operations on data, often in `SELECT`, `WHERE`, or `CASE` clauses.

    ---

    ### 🔹 Types of SQL Operators

    | Type                     | Description                                                | Example                                 |
    |--------------------------|------------------------------------------------------------|-----------------------------------------|
    | **1. Arithmetic**        | Perform math operations                                   | `salary + bonus`                        |
    | **2. Comparison**        | Compare values                                             | `age > 25`, `salary = 50000`            |
    | **3. Logical**           | Combine conditions                                         | `AND`, `OR`, `NOT`                      |
    | **4. Bitwise**           | Bit-level manipulation                                    | `a & b`, `a | b`                         |
    | **5. Set**               | Check membership in a set                                 | `IN`, `NOT IN`                          |
    | **6. EXISTS**            | Checks if a subquery returns rows                         | `EXISTS`, `NOT EXISTS`                  |
    | **7. BETWEEN**           | Range checking                                            | `BETWEEN 10 AND 20`                     |
    | **8. LIKE**              | Pattern matching                                           | `LIKE 'A%'`                             |
    | **9. NULL Check**        | Check for nulls                                            | `IS NULL`, `IS NOT NULL`                |

    ---

    ### 🔸 Examples

    ```sql
    -- Arithmetic
    SELECT salary + bonus FROM employees;

    -- Comparison
    SELECT * FROM employees WHERE age >= 30;

    -- Logical
    SELECT * FROM employees WHERE age > 25 AND department = 'Sales';

    -- Set
    SELECT * FROM employees WHERE department IN ('HR', 'IT');

    -- EXISTS
    SELECT name FROM employees e
    WHERE EXISTS (
    SELECT 1 FROM departments d WHERE d.id = e.department_id
    );

    -- BETWEEN
    SELECT * FROM employees WHERE salary BETWEEN 30000 AND 60000;

    -- LIKE
    SELECT * FROM employees WHERE name LIKE 'S%';

    -- NULL
    SELECT * FROM employees WHERE bonus IS NULL;
    ```


10. ### What is the difference between WHERE and HAVING clause

    `WHERE` and `HAVING` are both used to filter records in SQL, but they differ in **when** and **how** they are applied.

    ---

    ### ✅ WHERE Clause

    - 🔍 **Filters rows before grouping**
    - 🧱 Used with `SELECT`, `UPDATE`, `DELETE`
    - 🚫 Cannot be used with aggregate functions (`SUM()`, `COUNT()`, etc.)
    - 📍 Applied **before** `GROUP BY`

    ### 🔹 Example:
    ```sql
    SELECT * FROM employees
    WHERE department = 'Sales';
    ```

    ---

    ### ✅ HAVING Clause

    - 🔍 **Filters groups after aggregation**
    - 📊 Used **only** with `GROUP BY`
    - ✅ Can use aggregate functions like `COUNT()`, `AVG()`, etc.
    - 📍 Applied **after** `GROUP BY`

    ### 🔹 Example:
    ```sql
    SELECT department, COUNT(*) 
    FROM employees
    GROUP BY department
    HAVING COUNT(*) > 5;
    ```

    ---

    ### 📌 Key Differences

    | Feature         | WHERE                          | HAVING                           |
    |----------------|---------------------------------|----------------------------------|
    | When applied    | Before grouping                | After grouping                   |
    | Used with       | SELECT, UPDATE, DELETE         | SELECT (with GROUP BY)           |
    | Aggregates      | Cannot filter on aggregates    | Can filter on aggregates         |
    | Purpose         | Filter individual rows         | Filter grouped records           |

    ---

    ### ✅ Summary

    - Use `WHERE` to filter **individual rows**.
    - Use `HAVING` to filter **groups created by `GROUP BY`**.





11. ### What are Aggregate Functions in SQL

    **Aggregate functions** perform a calculation on a set of values and return a single value.  
    They are often used with the `GROUP BY` clause to group rows and summarize data.

    ---

    ### Common Aggregate Functions:

    | Function     | Description                                  |
    |--------------|----------------------------------------------|
    | `COUNT()`    | Counts the number of rows                    |
    | `SUM()`      | Adds up the values of a numeric column       |
    | `AVG()`      | Calculates the average of a numeric column   |
    | `MIN()`      | Returns the smallest value                   |
    | `MAX()`      | Returns the largest value                    |

    ---

    ### Example:

    #### 📌 Table: sales

    | id | product  | quantity | price |
    | -- | -------- | -------- | ----- |
    | 1  | Pen      | 10       | 5     |
    | 2  | Notebook | 5        | 20    |
    | 3  | Pencil   | 20       | 2     |
    | 4  | Eraser   | 15       | 3     |


    ---

    ### Query:

    ```sql
    SELECT 
    COUNT(*) AS total_items,
    SUM(quantity) AS total_quantity,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
    FROM sales;

    ```
    ### Output
    | total\_items | total\_quantity | avg\_price | min\_price | max\_price |
    | ------------ | --------------- | ---------- | ---------- | ---------- |
    | 4            | 50              | 7.5        | 2          | 20         |

        
5. ### Explain normalization and its types 1NF, 2NF, 3NF     
    ### Normalization in SQL

    ## ✅ What is Normalization?

    **Normalization** is a process in database design that:

    - Eliminates redundant data (repetition)
    - Ensures data integrity
    - Organizes data efficiently across tables

    It involves splitting large tables into smaller related tables and defining relationships between them.

    ---

    ### 🔹 First Normal Form (1NF)

    ### 🔸 Rule:
    - Each column should contain **atomic (indivisible)** values.
    - Each record should be **unique**.
    - No repeating groups or arrays allowed.

    ### ❌ Not in 1NF:

    | student_id | name  | subjects        |
    |------------|-------|-----------------|
    | 1          | Raj   | Math, Science   |
    | 2          | Priya | English         |

    ➡️ `subjects` column contains multiple values — violates atomicity.

    ### ✅ In 1NF:

    | student_id | name  | subject   |
    |------------|-------|-----------|
    | 1          | Raj   | Math      |
    | 1          | Raj   | Science   |
    | 2          | Priya | English   |

    ---

    ### 🔹 Second Normal Form (2NF)

    ### 🔸 Rule:
    - Must be in **1NF**.
    - All non-key columns must depend on the **entire** primary key (no **partial dependencies**).

    > Applies when the primary key is **composite** (more than one column).

    ### ❌ Not in 2NF:

    | student_id | subject   | student_name |
    |------------|-----------|--------------|
    | 1          | Math      | Raj          |
    | 1          | Science   | Raj          |
    | 2          | English   | Priya        |

    ➡️ `student_name` depends only on `student_id`, not on the full composite key (`student_id + subject`).

    ### ✅ In 2NF:

    **Students Table**

    | student_id | student_name |
    |------------|--------------|
    | 1          | Raj          |
    | 2          | Priya        |

    **Subjects Table**

    | student_id | subject   |
    |------------|-----------|
    | 1          | Math      |
    | 1          | Science   |
    | 2          | English   |

    ---

    ### 🔹 Third Normal Form (3NF)

    ### 🔸 Rule:
    - Must be in **2NF**.
    - No **transitive dependencies**: Non-key columns should not depend on **other non-key columns**.

    ### ❌ Not in 3NF:

    | student_id | student_name | city   | city_pincode |
    |------------|--------------|--------|--------------|
    | 1          | Raj          | Pune   | 411001       |
    | 2          | Priya        | Mumbai | 400001       |

    ➡️ `city_pincode` depends on `city`, which is a non-key column.

    ### ✅ In 3NF:

    **Students Table**

    | student_id | student_name | city   |
    |------------|--------------|--------|
    | 1          | Raj          | Pune   |
    | 2          | Priya        | Mumbai |

    **Cities Table**

    | city   | city_pincode |
    |--------|---------------|
    | Pune   | 411001        |
    | Mumbai | 400001        |

    ---

    ### 🎯 Summary

    | Normal Form | Rule                                                    |
    |-------------|---------------------------------------------------------|
    | 1NF         | Atomic values, no repeating groups                      |
    | 2NF         | No partial dependency on part of a composite key        |
    | 3NF         | No transitive dependency between non-key columns        |
    




12. ### What is a GROUP BY clause? How is it used with aggregate functions
    ### 🧮 SQL `GROUP BY` Clause Explained

    ### 📘 What is `GROUP BY`?
    The `GROUP BY`  is a clause in SQL used to group rows based on one or more columns.
    It is commonly used with **aggregate functions** like:
    - `COUNT()`
    - `SUM()`
    - `AVG()`
    - `MAX()`
    - `MIN()`

    ---

    ### 🧠 Purpose:
    To perform **aggregation** on groups of data rather than on the entire dataset.

    ---

    ### 📄 Example Table: `Sales`

    | sale_id | product  | region   | amount |
    |---------|----------|----------|--------|
    | 1       | Phone    | West     | 1000   |
    | 2       | Laptop   | East     | 1500   |
    | 3       | Phone    | West     | 1200   |
    | 4       | Phone    | East     | 900    |
    | 5       | Laptop   | East     | 1800   |

    ---

    ### 🔹 Example 1: Total Sales by Region

    ```sql
    SELECT region, SUM(amount) AS total_sales
    FROM Sales
    GROUP BY region;
    ```

    ### ✅ Output:

    | region | total_sales |
    |--------|-------------|
    | West   | 2200        |
    | East   | 4200        |

    ### 💡 Explanation:
    - The query groups rows by `region`.
    - It calculates the total `amount` for each region using `SUM()`.

    ---

    ### 🔹 Example 2: Count of Products Sold by Type

    ```sql
    SELECT product, COUNT(*) AS total_sold
    FROM Sales
    GROUP BY product;
    ```

    ### ✅ Output:

    | product | total_sold |
    |---------|------------|
    | Phone   | 3          |
    | Laptop  | 2          |

    ---

    ### ⚠️ Notes:
    - All columns in the `SELECT` statement **must be either in `GROUP BY`** or **aggregated**.
    - You can combine `GROUP BY` with `HAVING` to filter grouped results.

    ---

    ### 🔹 Example with `HAVING`:
    ```sql
    SELECT region, SUM(amount) AS total_sales
    FROM Sales
    GROUP BY region
    HAVING SUM(amount) > 3000;
    ```

    ### ✅ Output:

    | region | total_sales |
    |--------|-------------|
    | East   | 4200        |

    ➡️ Only regions with sales greater than 3000 are shown.

    ---

    > 📌 The `GROUP BY` clause is essential for summarizing and analyzing data across categories or groups.






13. ### What is a subquery, Explain with an example

    ### 🔍 What is a Subquery in SQL?

    ### 🧠 Definition:
    A **subquery** (also known as an **inner query** or **nested query**) is a query **within another SQL query**.  
    It is enclosed in parentheses and is used to return data that will be used by the **main (outer) query**.

    ---

    ### ✅ Use Cases:
    - Filtering rows (`WHERE` clause)
    - Creating derived columns (`SELECT` clause)
    - Replacing JOINs (in some cases)
    - Used in `INSERT`, `UPDATE`, and `DELETE` as well

    ---

    ### 🔄 Types of Subqueries:
    1. **Scalar Subquery** – Returns a single value.
    2. **Row Subquery** – Returns a single row.
    3. **Table Subquery** – Returns a table (used with `IN`, `EXISTS`, or joins).
    4. **Correlated Subquery** – References a column from the outer query.

    ---

    ### 📄 Example Table: `Employee`

    | emp_id | emp_name | salary |
    |--------|----------|--------|
    | 1      | Raj      | 50000  |
    | 2      | Riya     | 60000  |
    | 3      | Aman     | 70000  |
    | 4      | Neha     | 60000  |

    ---

    ### 🔹 Example: Find employees who earn more than the **average salary**

    ### 🧾 Query:
    ```sql
    SELECT emp_name, salary
    FROM Employee
    WHERE salary > (
        SELECT AVG(salary)
        FROM Employee
    );
    ```

    ### 💡 Explanation:
    - The **subquery** `(SELECT AVG(salary) FROM Employee)` calculates the average salary.
    - The **main query** selects employees whose salary is **greater** than this average.

    ---

    ### 🧮 Output:

    | emp_name | salary |
    |----------|--------|
    | Aman     | 70000  |

    ---

    > ✅ Subqueries are powerful tools in SQL that allow you to break complex problems into simpler parts.





14. ### What is difference between Group by and order by
    The GROUP BY clause in SQL is used to arrange identical data into groups based on one or more columns. It is typically used in conjunction with aggregate functions such as COUNT(), SUM(), AVG(), MAX(), and MIN() to perform summary operations on grouped data.

    | GROUP BY                                                   | ORDER BY                                                     |
    |------------------------------------------------------------|--------------------------------------------------------------|
    | Used to **group rows** based on the same values in one or more columns. | Used to **sort the result set** in ascending or descending order. |
    | Always used with **aggregate functions** like `COUNT()`, `SUM()`, `AVG()` | Does **not require** aggregate functions.                   |
    | Comes **before ORDER BY** in query syntax.                 | Comes **after GROUP BY** if both are used.                  |
    | Groups the result into **summary rows**.                   | Sorts the **entire result set**.                            |
    | Example: Group sales by product category.                  | Example: Sort sales by highest to lowest amount.            |



15. ### What are the different types of joins in SQL
    Joins in SQL are used to combine data from two or more tables based on a related column
    between them.

    #### Types of Joins:

    1. INNER JOIN – Returns only matching rows from both tables.
    2. LEFT JOIN – Returns all rows from the left table and matching rows from the right table.
    3. RIGHT JOIN – Returns all rows from the right table and matching rows from the left
        table.
    4. FULL JOIN – Returns all rows from both tables (matching and non-matching).
    5. CROSS JOIN – Returns the Cartesian product of both tables (all possible combinations).
    6. SELF JOIN – Joins a table with itself.

    ### INNER JOIN

    Returns only the rows where there is a match in both tables.

    ---

    ### Sample Tables:

    **Employees**

    | emp_id | emp_name |
    |--------|----------|
    | 1      | Raj      |
    | 2      | Riya     |
    | 3      | Aman     |
    | 4      | Neha     |

    **Departments**

    | emp_id | dept_name  |
    |--------|------------|
    | 1      | Sales      |
    | 2      | HR         |
    | 5      | Marketing  |

    ---

    ### Query:
    ```sql
    SELECT E.emp_name, D.dept_name
    FROM Employees E
    INNER JOIN Departments D ON E.emp_id = D.emp_id;
    ```
    **Output** **Table**

    | emp_name | dept_name |
    |----------|-----------|
    | Raj      | Sales     |
    | Riya     | HR        |


    ---
    ### LEFT JOIN (LEFT OUTER JOIN)

    Returns all rows from the **left table** (`Employees`) and the **matched rows** from the right table (`Departments`).  
    If there is **no match**, the result is `NULL` on the right side.

    ---

    ### Sample Tables:

    **Employees**

    | emp_id | emp_name |
    |--------|----------|
    | 1      | Raj      |
    | 2      | Riya     |
    | 3      | Aman     |
    | 4      | Neha     |

    **Departments**

    | emp_id | dept_name  |
    |--------|------------|
    | 1      | Sales      |
    | 2      | HR         |
    | 5      | Marketing  |

    ---

    ### Query:

    ```sql
    SELECT E.emp_name, D.dept_name
    FROM Employees E
    LEFT JOIN Departments D ON E.emp_id = D.emp_id;
    ```
    ### Output
    | emp\_name | dept\_name |
    | --------- | ---------- |
    | Raj       | Sales      |
    | Riya      | HR         |
    | Aman      | NULL       |
    | Neha      | NULL       |


    ---
    ### RIGHT JOIN (RIGHT OUTER JOIN)

    Returns all rows from the **right table** (`Departments`) and the **matched rows** from the left table (`Employees`).  
    If there is **no match**, the result is `NULL` on the left side.

    ---

    ### Sample Tables:

    **Employees**

    | emp_id | emp_name |
    |--------|----------|
    | 1      | Raj      |
    | 2      | Riya     |
    | 3      | Aman     |
    | 4      | Neha     |

    **Departments**

    | emp_id | dept_name  |
    |--------|------------|
    | 1      | Sales      |
    | 2      | HR         |
    | 5      | Marketing  |

    ---

    ### Query:

    ```sql
    SELECT E.emp_name, D.dept_name
    FROM Employees E
    RIGHT JOIN Departments D ON E.emp_id = D.emp_id;
    ```

    ### Output
    | emp\_name | dept\_name |
    | --------- | ---------- |
    | Raj       | Sales      |
    | Riya      | HR         |
    | NULL      | Marketing  |

    ---

    ### FULL OUTER JOIN

    Returns **all rows** from both tables.  
    Where there is no match, the result will have `NULL` for the missing side.

    > 🔸 **Note**: MySQL does **not support FULL OUTER JOIN directly**.  
    > You can simulate it using a `UNION` of `LEFT JOIN` and `RIGHT JOIN`.

    ---

    ### Sample Tables:

    **Employees**

    | emp_id | emp_name |
    |--------|----------|
    | 1      | Raj      |
    | 2      | Riya     |
    | 3      | Aman     |
    | 4      | Neha     |

    **Departments**

    | emp_id | dept_name  |
    |--------|------------|
    | 1      | Sales      |
    | 2      | HR         |
    | 5      | Marketing  |

    ---

    ### Query (Simulated FULL OUTER JOIN in MySQL):

    ```sql
    SELECT E.emp_name, D.dept_name
    FROM Employees E
    LEFT JOIN Departments D ON E.emp_id = D.emp_id

    UNION

    SELECT E.emp_name, D.dept_name
    FROM Employees E
    RIGHT JOIN Departments D ON E.emp_id = D.emp_id;

    ```
    ### Output
    | emp\_name | dept\_name |
    | --------- | ---------- |
    | Raj       | Sales      |
    | Riya      | HR         |
    | Aman      | NULL       |
    | Neha      | NULL       |
    | NULL      | Marketing  |


    ---

    ### CROSS JOIN

    Returns the **Cartesian product** of both tables, i.e., every combination of rows from the left and right tables.  
    If one table has `m` rows and the other has `n`, the result will have `m × n` rows.

    ---

    ### Sample Tables:

    **Employees**

    | emp_id | emp_name |
    |--------|----------|
    | 1      | Raj      |
    | 2      | Riya     |
    | 3      | Aman     |
    | 4      | Neha     |

    **Departments**

    | emp_id | dept_name  |
    |--------|------------|
    | 1      | Sales      |
    | 2      | HR         |
    | 5      | Marketing  |

    ---

    ### Query:

    ```sql
    SELECT E.emp_name, D.dept_name
    FROM Employees E
    CROSS JOIN Departments D;
    ```
    ### Output
    | emp\_name | dept\_name |
    | --------- | ---------- |
    | Raj       | Sales      |
    | Raj       | HR         |
    | Raj       | Marketing  |
    | Riya      | Sales      |
    | Riya      | HR         |
    | Riya      | Marketing  |
    | Aman      | Sales      |
    | Aman      | HR         |
    | Aman      | Marketing  |
    | Neha      | Sales      |
    | Neha      | HR         |
    | Neha      | Marketing  |


    ---

    ### SELF JOIN

    A **SELF JOIN** is a regular join where a table is joined with **itself**.  
    Useful for comparing rows within the same table (e.g., hierarchical relationships).

    ---

    ### Sample Table: Employees

    | emp_id | emp_name |
    |--------|----------|
    | 1      | Raj      |
    | 2      | Riya     |
    | 3      | Aman     |
    | 4      | Neha     |

    ---

    ### Query:

    ```sql
    SELECT A.emp_name AS Employee, B.emp_name AS Manager
    FROM Employees A
    JOIN Employees B ON A.emp_id = B.emp_id - 1;
    ```
    ### Output
    | Employee | Manager |
    | -------- | ------- |
    | Riya     | Raj     |
    | Aman     | Riya    |
    | Neha     | Aman    |

    ---

    ### OUTER JOIN (General Term)

    **OUTER JOIN** is a general category of joins that includes:

    - **LEFT OUTER JOIN**
    - **RIGHT OUTER JOIN**
    - **FULL OUTER JOIN**

    These joins are used when you want to:

    ✅ Retrieve **all data** from one or both tables,  
    ✅ Include **unmatched rows** by filling in `NULL` where no match exists.

    ---

    ### Comparison Table

    | Join Type        | Description                                                    |
    |------------------|----------------------------------------------------------------|
    | LEFT OUTER JOIN  | All rows from the left table + matched rows from the right     |
    | RIGHT OUTER JOIN | All rows from the right table + matched rows from the left     |
    | FULL OUTER JOIN  | All rows from both tables, matched and unmatched rows          |

    ---

    **Use Case:**  
    Use OUTER JOINs when you need a **complete picture**, including data that doesn’t match between tables.







16. ### What is the difference between UNION and UNION ALL
    UNION and UNION ALL are used to combine the result sets of two or more SELECT
    statements.

    ### 🧾 Difference Between `UNION` and `UNION ALL` in SQL

    | `UNION`                                                | `UNION ALL`                                           |
    |--------------------------------------------------------|-------------------------------|
    | Removes duplicate rows from the result set.           | Includes **all rows**, even if duplicates exist.       |
    | Slower, due to duplicate elimination and sorting.     | Faster, as it skips duplicate checking.                |
    | Use when you need only **unique** results.            | Use when you want to **preserve all rows**, including duplicates. |
    | Performs internal sorting to remove duplicates.       | No sorting is performed.                              |
    | Smaller, if duplicates exist.                         | Larger, as it contains all entries.                    |



    ### 🔹 Example Tables

    **Table A:**
    | id | city     |
    |----|----------|
    | 1  | Mumbai   |
    | 2  | Delhi    |
    | 3  | Kolkata  |

    **Table B:**
    | id | city     |
    |----|----------|
    | 1  | Delhi    |
    | 2  | Chennai  |
    | 3  | Mumbai   |



    ### 🔹 `UNION` Query
    ```sql
    SELECT city FROM A
    UNION
    SELECT city FROM B;
    ```

    **Output:**
    | city     |
    |----------|
    | Mumbai   |
    | Delhi    |
    | Kolkata  |
    | Chennai  |

    ✅ Duplicates like "Mumbai" and "Delhi" are removed.



    ### 🔹 `UNION ALL` Query
    ```sql
    SELECT city FROM A
    UNION ALL
    SELECT city FROM B;
    ```

    **Output:**
    | city     |
    |----------|
    | Mumbai   |
    | Delhi    |
    | Kolkata  |
    | Delhi    |
    | Chennai  |
    | Mumbai   |

    ✅ All rows are returned including duplicates.



    ### ✅ Summary

    - Use `UNION` when you want unique records from multiple queries.
    - Use `UNION ALL` when performance is important or duplicates are meaningful for your logic.




17. ### What is the difference between UNION and JOIN
    | `UNION`                                            | `JOIN`                                                |
    |----------------------------------------------------|--------------------------------------------------------|
    | Combines **rows from two queries** into a single result set | Combines **columns from two or more tables**            |
    | Stacks results **vertically**                      | Merges results **horizontally** based on a condition   |
    | Requires same number of columns and compatible data types | Can join on keys even if column counts/types differ     |
    | Removes duplicates by default (`UNION ALL` keeps them) | Does not remove duplicates unless specified             |
    | Each query runs separately and results are merged  | Tables are scanned and matched row by row              |




18. ### What is CASE Statement in SQL
    The CASE Statement is used to apply conditional logic in SQL queries, similar to IF-ELSE
    statements.

    It checks conditions one by one, and returns a value based on which condition is true — useful when you want custom outputs in your SELECT queries

    - Its is use to categorize data based on condition
    - To add logic inside queries without changing the table
    **General Syntax**
    ```sql
    SELECT
    column,
    CASE
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        ...
        ELSE default_result
    END AS alias_name
    FROM table_name;

    ```

    **✅ Example:**
    Suppose you have a students table with marks column:
    ```sql
    SELECT name, marks,
    CASE
        WHEN marks >= 90 THEN 'A+'
        WHEN marks >= 75 THEN 'A'
        WHEN marks >= 60 THEN 'B'
        ELSE 'C'
    END AS grade
    FROM students;

    ```
    📌 This will assign grades based on marks dynamically in the output.

    🪄 Output Example:

    | name   | marks | grade |
    | ------ | ----- | ----- |
    | Suhas  | 91    | A+    |
    | Rutuja | 77    | A     |
    | Chirag | 58    | C     |

    **🧩 Notes:**
    - You can use CASE in SELECT, WHERE, ORDER BY, even in UPDATE

    - ELSE is optional — if omitted and no conditions match, result is NULL

    - You can nest CASE statements inside one another




19. ### How to handle NULL values in SQL
    NULL represents missing or unknown data in SQL
    >NULL means no value or unknown data. It is not the same as 0, '', or " ".

    **🔍 1. Check if a value is NULL**
    ```sql
    SELECT * FROM table_name
    WHERE column_name IS NULL;

    ```

    **Or to check not null:**
    ```sql
    SELECT * FROM table_name
    WHERE column_name IS NOT NULL;


    ```

    **🎯 2. Replace NULL using IFNULL() (MySQL-specific)**

    ```sql
    SELECT name, IFNULL(email, 'No Email') AS email_status
    FROM users;

    ```
    📌 This shows "No Email" wherever email is NULL


    **🔁 3. Replace NULL using COALESCE() (Standard SQL)**
    ```sql
    SELECT name, COALESCE(phone, 'Not Provided') AS phone_status
    FROM customers;

    ```
    📌 COALESCE() returns the first non-null value.




20. ### How to Optimize SQL Queries
    **Optimizing SQL queries helps improve performance, speed, and efficiency of your database operations.**
    | Technique                         | Description                                                                 |
    |----------------------------------|-----------------------------------------------------------------------------|
    | Use SELECT Only What You Need    | Avoid `SELECT *`. Fetch only necessary columns to reduce load.             |
    | Use Proper Indexing              | Create indexes on columns used in `WHERE`, `JOIN`, `ORDER BY`, etc.        |
    | Use WHERE Clauses Effectively    | Always filter rows early to reduce scanned data.                           |
    | Avoid Redundant Joins            | Don’t use joins if the data can be fetched from one table.                 |
    | Use LIMIT for Large Tables       | Fetch limited rows when testing or displaying previews.                    |
    | Avoid Functions in WHERE         | Use raw column comparisons instead of functions on columns (`YEAR(date)` is slow). |
    | Use EXISTS Instead of IN         | For large subqueries, `EXISTS` is usually faster than `IN`.                |
    | Use UNION ALL If Duplicates OK   | `UNION ALL` skips the duplicate check, which saves time.                   |
    | Analyze Query with EXPLAIN       | Use `EXPLAIN` before your query to see how MySQL processes it.             |
    | Normalize the Schema             | Remove redundancy to keep queries cleaner and indexes more effective.      |




21. ### What is the difference between IN and EXISTS

    | `IN`                                               | `EXISTS`                                                  |
    |----------------------------------------------------|------------------------------------------------------------|
    | Compares a value to a list or result set           | Checks for the existence of rows returned by a subquery    |
    | Returns TRUE if value is found in the list         | Returns TRUE if at least one row is returned               |
    | Slower on large subqueries                         | Faster on large subqueries (especially with indexes)       |
    | Best for static or small subqueries                | Best for correlated subqueries or large datasets           |
    | Affected by NULLs in subquery                      | Not affected by NULLs in subquery                          |








22. ### what is normalization and denormalization.
    #### Defination: 
    Normalization is the process of organizing data in a database to reduce redundancy and
    improve data integrity. It involves dividing large tables into smaller related tables and defining
    relationships between them.

    #### Key Features:
    - Reduces data redundancy
    - Improves data consistency
    - Simplifies data maintenance
    - Increases data integrity

    **Types of Normalization:**
    1. 1NF (First Normal Form) – Eliminates duplicate columns and ensures each column contains
    atomic values.
    2. 2NF (Second Normal Form) – Ensures no partial dependency by making all non-key
    attributes fully dependent on the primary key.
    3. 3NF (Third Normal Form) – Removes transitive dependencies where non-key columns
    depend on other non-key columns.
    4. BCNF (Boyce-Codd Normal Form) – Ensures that every determinant is a candidate key.

    #### Example
    **❌ Unnormalized Table (Bad Design)**
    | student_id | name   | courses                  |
    |------------|--------|--------------------------|
    | 1          | Suhas  | Math, Physics, Chemistry |
    | 2          | Rutuja | Math                     |

    🔴 Problems:
    courses is not atomic → violates 1NF


    **✅ 1NF – First Normal Form**
    | student_id | name   | course     |
    |------------|--------|------------|
    | 1          | Suhas  | Math       |
    | 1          | Suhas  | Physics    |
    | 1          | Suhas  | Chemistry  |
    | 2          | Rutuja | Math       |

    Each value is atomic (one course per row)

    **✅ 2NF – Second Normal Form**

    📄 `students` table:

    | student_id | name   |
    |------------|--------|
    | 1          | Suhas  |
    | 2          | Rutuja |

    📄 `student_courses` table:

    | student_id | course     |
    |------------|------------|
    | 1          | Math       |
    | 1          | Physics    |
    | 1          | Chemistry  |
    | 2          | Math       |

    ✅ Removed partial dependency (name depends only on student_id)

    **✅ 3NF – Third Normal Form**
    📄 `students` table:

    | student_id | name   |
    |------------|--------|
    | 1          | Suhas  |
    | 2          | Rutuja |

    📄 `courses` table:

    | course     | department |
    |------------|------------|
    | Math       | Science    |
    | Physics    | Science    |
    | Chemistry  | Science    |

    📄 `student_courses` table:

    | student_id | course     |
    |------------|------------|
    | 1          | Math       |
    | 1          | Physics    |
    | 1          | Chemistry  |
    | 2          | Math       |

    ✅ Removed transitive dependency (department doesn't depend on student anymore)

    #### ✅ Summary of Normal Forms
    | Normal Form | Rule                                    | Fix                                  |
    | ----------- | --------------------------------------- | ------------------------------------ |
    | 1NF         | Remove multivalued (non-atomic) columns | Separate values into individual rows |
    | 2NF         | Remove partial dependencies             | Split repeating group into new table |
    | 3NF         | Remove transitive dependencies          | Isolate attributes into new tables   |










23. ### What is INDEX
    An Index in SQL is like a shortcut. It helps the database find data faster without scanning the entire table.

    📌 Without index: SQL checks every row one by one (slow).

    📌 With index: SQL jumps directly to the matching row (fast).

    #### 🧱 What is a Clustered Index?
    A Clustered Index sorts and stores the actual table data based on the indexed column.

    Data is physically stored in sorted order.

    You can have only one clustered index per table.

    Primary Key creates a clustered index by default.
    **Example**
    ```sql
    CREATE TABLE students (
    id INT PRIMARY KEY,   -- Clustered index
    name VARCHAR(50)
    );

    ```
    | id | name   |
    |----|--------|
    | 1  | Suhas  |
    | 2  | Rutuja |
    | 3  | Kewal  |

    So when you search id = 2, SQL finds it very quickly.




    #### 📘 What is a Non-Clustered Index?
    A Non-Clustered Index is a separate structure that holds column values and points to their rows in the table.

    The data is NOT sorted in the table.

    You can create many non-clustered indexes.

    It helps with fast lookups on non-key columns.

    **🟡 How to Use a Non-Clustered Index in SQL**
    Once you create a non-clustered index, MySQL will automatically use it when your query filters or sorts by that indexed column.
    Example
    1. Create the table:
    ```sql

    CREATE TABLE students (
    student_id INT PRIMARY KEY,     -- clustered index
    name VARCHAR(50),
    city VARCHAR(50)
    );

    ```

    2. Create a non-clustered index on name:
    ```sql
    CREATE INDEX idx_name ON students(name);

    ```
    This creates a non-clustered index on the name column.


    **🎯 How to Use It?**
    Just write a query using the indexed column — MySQL will use the index automatically.
    ```sql
    -- Uses the non-clustered index on name
    SELECT * FROM students WHERE name = 'Rutuja';

    ```
    💡 This query is faster than without index, especially on large tables.


    **🔍 Want to check if index is used?**
    Use EXPLAIN:
    ```sql
    EXPLAIN SELECT * FROM students WHERE name = 'Rutuja';

    ```
    ➡️ The output will show something like:

    | id | select\_type | table    | type | possible\_keys | key       | key\_len | ref   | rows | Extra       |
    | -- | ------------ | -------- | ---- | -------------- | --------- | -------- | ----- | ---- | ----------- |
    | 1  | SIMPLE       | students | ref  | idx\_name      | idx\_name | 153      | const | 1    | Using index |

    **📌 What Helps Index Usage?**
    Queries with WHERE name = ...

    ORDER BY name

    JOIN using name

    SELECT name FROM ... with filtering


    **⚠️ Reminder:**
    - Non-clustered index ≠ automatic for every query

    - It is used only when your query uses that column in a way that benefits performance










































































---


## 🔹 Query Questions


1. ### Write a query to find the second highest salary from an Employee table


    ### 📝 Problem:
    Write a query to return the **second highest salary** from the `Employee` table.

    ---

    ### 📄 Table: `Employee`

    | emp_id | emp_name | salary |
    |--------|----------|--------|
    | 1      | Raj      | 50000  |
    | 2      | Riya     | 60000  |
    | 3      | Aman     | 70000  |
    | 4      | Neha     | 60000  |

    ---

    ### ✅ Query (Using `DISTINCT` + `ORDER BY` + `LIMIT` with `OFFSET`):
    ```sql
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1;
    ```

    ### 🔍 Explanation:
    - `DISTINCT` ensures that duplicate salaries are not counted multiple times.
    - `ORDER BY salary DESC` sorts salaries from highest to lowest.
    - `LIMIT 1 OFFSET 1` skips the highest salary (offset 1) and returns the next one (second highest).

    ---

    ## ✅ Alternate Query (Using Subquery):
    ```sql
    SELECT MAX(salary)
    FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee);
    ```

    ### 🔍 Explanation:
    - First, it finds the maximum salary.
    - Then, it gets the highest salary **less than the maximum**, which is the second highest.




## Advance Interview question
1. ### What are window functions, How do you use RANK(), DENSE_RANK(), ROW_NUMBER()

    ### Window Functions in SQL

    ### 🔹 What are Window Functions?

    A Window Function performs a calculation on a set of rows related to the current row without combining them into a single result.

    **🔑 Key Points (Simplified):**
    - Works with the OVER() clause

    - Keeps individual rows — does not group like GROUP BY

    - Useful for ranking, running totals, moving averages, etc.




    ---

    ### 📌 Syntax:

    ```sql
    function_name() OVER (
        PARTITION BY column
        ORDER BY column
    )
    ```

    ### 1. `ROW_NUMBER()`

    Assigns a **unique, sequential number** to each row within the partition or full result set.

    ---

    ### 🔸 Example Query:

    ```sql
    SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
    FROM Employees;
    ```
    ### Sample Table: Employees
    | emp\_id | name | department | salary |
    | ------- | ---- | ---------- | ------ |
    | 1       | Raj  | Sales      | 50000  |
    | 2       | Riya | Sales      | 60000  |
    | 3       | Aman | Sales      | 60000  |
    | 4       | Neha | Sales      | 40000  |

    ### Output
    | name | salary | row\_num |
    | ---- | ------ | -------- |
    | Riya | 60000  | 1        |
    | Aman | 60000  | 2        |
    | Raj  | 50000  | 3        |
    | Neha | 40000  | 4        |




    ### 2. `RANK()`

    Assigns a **rank to each row** based on the order specified.  
    Rows with **equal values** get the **same rank**, and the **next rank is skipped**.

    ---

    ### 🔸 Example Query:

    ```sql
    SELECT name, salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
    FROM Employees;
    ```
    ###  Sample Table: Employees
    | emp\_id | name | department | salary |
    | ------- | ---- | ---------- | ------ |
    | 1       | Raj  | Sales      | 50000  |
    | 2       | Riya | Sales      | 60000  |
    | 3       | Aman | Sales      | 60000  |
    | 4       | Neha | Sales      | 40000  |

    ### Output
    | name | salary | rank |
    | ---- | ------ | ---- |
    | Riya | 60000  | 1    |
    | Aman | 60000  | 1    |
    | Raj  | 50000  | 3    |
    | Neha | 40000  | 4    |

    ### 3. `DENSE_RANK()`

    Assigns a **rank like `RANK()`**, but **does not skip** the next rank after ties.

    ---

    ### 🔸 Example Query:

    ```sql
    SELECT name, salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
    FROM Employees;
    ```

    ### Sample Table: Employees
    | emp\_id | name | department | salary |
    | ------- | ---- | ---------- | ------ |
    | 1       | Raj  | Sales      | 50000  |
    | 2       | Riya | Sales      | 60000  |
    | 3       | Aman | Sales      | 60000  |
    | 4       | Neha | Sales      | 40000  |

    ### Output
    | name | salary | dense\_rank |
    | ---- | ------ | ----------- |
    | Riya | 60000  | 1           |
    | Aman | 60000  | 1           |
    | Raj  | 50000  | 2           |
    | Neha | 40000  | 3           |

    ### 🔚 Summary: ROW_NUMBER vs RANK vs DENSE_RANK

    | Function     | Handles Ties | Skips Ranks? | Unique Values? | Example Use Case                          |
    |--------------|--------------|--------------|----------------|-------------------------------------------|
    | `ROW_NUMBER` | ❌ No         | N/A          | ✅ Yes         | To assign a unique number to each row     |
    | `RANK`       | ✅ Yes        | ✅ Yes        | ❌ No          | When you want tied ranks but skip values  |
    | `DENSE_RANK` | ✅ Yes        | ❌ No         | ❌ No          | When you want tied ranks without skipping |

    - **Ties** = multiple rows with same value in ORDER BY column.
    - **Skips Ranks** = rank jumps after ties (`RANK()`).
    - **Unique Values** = whether the rank is always different per row.



2. ### Explain CTE (Common Table Expression) and its benefits

    ### ✅ Common Table Expression (CTE)

    ### 🔹 What is a CTE?

    A **Common Table Expression (CTE)** is a temporary, named result set in SQL.

    It is defined using the `WITH` clause and exists only during the execution of a single query.  
    CTEs are useful to:
    - Simplify complex queries
    - Improve readability
    - Enable recursive logic

    A CTE is **not stored** as a database object — it's a query helper.


    ### 📌 CTE Syntax

    The general syntax for defining and using a CTE:

    ```sql
    WITH cte_name AS (
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition
    )
    SELECT * FROM cte_name;
    ```

    ### ✅ Benefits of Using CTEs

    CTEs offer several advantages over subqueries and derived tables:

    | Benefit                 | Description                                                                 |
    |-------------------------|-----------------------------------------------------------------------------|
    | 1. Readability          | Makes complex queries easier to understand and maintain.                    |
    | 2. Modularity           | Breaks down logic into logical building blocks.                             |
    | 3. Reusability          | A CTE can be referenced multiple times in the same query.                   |
    | 4. Recursive Capability | Supports recursion to handle hierarchical or tree-structured data.          |
    | 5. Debugging Ease       | Easier to isolate and debug parts of the query logic.                       |



    ### 🔸 Example of a CTE

    Suppose you want to find employees earning more than ₹50,000.

    ### 👇 Query Using a CTE:

    ```sql
    WITH HighEarners AS (
    SELECT name, salary
    FROM Employees
    WHERE salary > 50000
    )
    SELECT * FROM HighEarners;
    ```


3. ### How do transactions work in SQL? What are ACID properties

    #### Transaction in SQL
    A transaction in SQL is a sequence of one or more SQL operations (such as INSERT, UPDATE, DELETE) that are executed as a single unit of work.

    A transaction ensures that either all the operations are successfully completed, or none of them take effect — maintaining data integrity.

    **Example**
    | student_id | name   | city         |
    |------------|--------|--------------|
    | 1          | Suhas  | Pune         |
    | 2          | Rutuja | Nagpur       |
    | 3          | Kewal  | Mumbai       |
    | 4          | Chirag | Nanded       |
    | 5          | Sonal  | Aurangabad   |

    **🔄 Option 1: Rollback Transaction**
    ```sql
    -- 🚦 Start the transaction
    START TRANSACTION;

    -- 🔄 Update student's city
    UPDATE students SET city = 'Mumbai' WHERE student_id = 1;

    -- 🗑️ Delete a student
    DELETE FROM students WHERE student_id = 5;

    -- ❌ Something went wrong
    ROLLBACK;

    -- 🔙 No changes are saved to database
    ```

    **✅ Option 2: Commit Transaction**
    ```sql
    -- 🚦 Start the transaction
    START TRANSACTION;

    -- 🔄 Update student's city
    UPDATE students SET city = 'Mumbai' WHERE student_id = 1;

    -- 🗑️ Delete a student
    DELETE FROM students WHERE student_id = 5;

    -- ✅ All good, save the changes
    COMMIT;

    -- 💾 Changes are now permanent


    ```



    #### **ACID property**
    | Property    | Full Form   | Description                                                                 |
    |-------------|-------------|-----------------------------------------------------------------------------|
    | A           | Atomicity   | Transaction is all or nothing. If any part fails, entire transaction is rolled back. |
    | C           | Consistency | Ensures data is valid and the database remains in a consistent state before and after transaction. |
    | I           | Isolation   | Transactions run independently without affecting each other.               |
    | D           | Durability  | Once committed, changes are permanent — even after a crash.                |


    ### 🔹 ACID Properties in SQL

    - **Atomicity**: Either both updates succeed or none.
    - **Consistency**: The total money in the system remains the same.
    - **Isolation**: Other users don’t see this half-completed transfer.
    - **Durability**: Once committed, the transfer is never lost.



4. ### What is the difference between IN and EXISTS

    ### 🔍 Difference Between `IN` and `EXISTS` in SQL

    ### ✅ Comparison Table

    | Feature         | `IN`                                                                 | `EXISTS`                                                             |
    |-----------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
    | **Definition**  | Checks if a value matches any value in a list or subquery            | Checks for the **existence** of rows returned by a subquery          |
    | **Execution**   | Subquery is executed **once**, then used for filtering               | Subquery is executed **for each row** in the outer query             |
    | **Performance** | Better for **small** datasets                                         | Better for **large** datasets or when the subquery uses indexes      |
    | **NULL Handling** | May behave unexpectedly with **NULLs**                            | Handles NULLs more predictably                                       |
    | **Best For**    | Comparing a value against a **list of values**                       | Checking if **rows exist** that satisfy a condition                  |

    ---

    ### 🔸 Example Using `IN`:

    ```sql
    SELECT name
    FROM employees
    WHERE department_id IN (
        SELECT id
        FROM departments
        WHERE location = 'Mumbai'
    );
    ```





    ### 🔸 Example Using `EXISTS`:

    ```sql
    SELECT name
    FROM employees e
    WHERE EXISTS (
        SELECT 1
        FROM departments d
        WHERE d.id = e.department_id
        AND d.location = 'Mumbai'
    );
    ```

5. ### Explain stored procedures, triggers, and views
    ### ✅ 1. Stored Procedure

    A **Stored Procedure** is a precompiled collection of one or more SQL statements stored in the database.

    ### 🔹 Features:
    - Improves performance through precompilation.
    - Promotes reusability.
    - Allows parameterized input/output.

    ### 🔸 Example:
    ```sql
    CREATE PROCEDURE GetEmployeeByDept(IN dept_id INT)
    BEGIN
        SELECT * FROM employees WHERE department_id = dept_id;
    END;
    ```

    ### ✅ 2. Trigger

    A **Trigger** is a special type of stored procedure that **automatically executes** in response to certain events on a table (such as INSERT, UPDATE, or DELETE).

    ### 🔹 Features:
    - Enforces business rules automatically.
    - Automatically logs or audits changes.
    - Cannot be manually called like regular procedures.

    ### 🔸 Example:
    ```sql
    CREATE TRIGGER log_salary_update
    AFTER UPDATE ON employees
    FOR EACH ROW
    BEGIN
        INSERT INTO salary_log(emp_id, old_salary, new_salary)
        VALUES (OLD.id, OLD.salary, NEW.salary);
    END;
    ```


    ### ✅ 3. View

    A **View** is a virtual table created by a SQL query. It does not store data physically but allows querying as if it were a real table.

    ### 🔹 Features:
    - Simplifies complex SQL queries.
    - Enhances data security by exposing only selected columns.
    - Can be used in SELECT statements like regular tables.

    ### 🔸 Example:
    ```sql
    CREATE VIEW SalesSummary AS
    SELECT salesperson_id, SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY salesperson_id;
    ```




6. ### What is the purpose of ALter Command

    ### ✅ ALTER Command in SQL

    The `ALTER` command in SQL is used to **modify the structure** of an existing database table.

    You can:
    - Add, delete, or modify columns
    - Rename columns or the table itself
    - Add or remove constraints


    ### 🔹 Syntax & Examples

    #### 🔸 Add a new column:
    ```sql
    ALTER TABLE employees ADD hire_date DATE;
    ```

    🔸 Modify a column:
    ```sql
    ALTER TABLE employees MODIFY salary DECIMAL(10,2);
    ```


    🔸 Rename a column (MySQL):
    ```sql
    ALTER TABLE employees RENAME COLUMN emp_name TO employee_name;

    ```

    🔸 Drop a column:
    ```sql
    ALTER TABLE employees DROP COLUMN hire_date;

    ```


    🔸 Rename a table:
    ```sql
    ALTER TABLE employees RENAME TO staff;
    ```



7. ### What Order of Execution of SQL Clauses
    ### ✅ Order of Execution of SQL Clauses

    SQL follows a specific **logical execution order**, which is different from the written order in queries.

    ### 🔢 Execution Order:

    | Step | Clause        | Description                                                                 |
    |------|---------------|-----------------------------------------------------------------------------|
    | 1    | `FROM`        | Defines source tables and joins.                                            |
    | 2    | `WHERE`       | Filters rows before grouping.                                               |
    | 3    | `GROUP BY`    | Groups rows based on specified columns.                                     |
    | 4    | `HAVING`      | Filters groups after aggregation.                                           |
    | 5    | `SELECT`      | Selects columns or expressions to return.                                   |
    | 6    | `DISTINCT`    | Removes duplicate rows from the result.                                     |
    | 7    | `ORDER BY`    | Sorts the final result.                                                     |
    | 8    | `LIMIT/OFFSET`| Restricts number of rows returned.                                          |

    ---

    ### 🔍 Example:
    ```sql
    SELECT department, COUNT(*) AS emp_count
    FROM employees
    WHERE status = 'Active'
    GROUP BY department
    HAVING COUNT(*) > 5
    ORDER BY emp_count DESC
    LIMIT 10;
    ```


