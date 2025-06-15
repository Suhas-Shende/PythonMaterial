## Basic Level Questions

1. ### What is SQL?

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

2. ### What are the different types of SQL statements
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



3. ### What is the difference between WHERE and HAVING clause

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

4. ### What is a primary key and foreign key


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


5. ### What is INDEX
    ### 📘 What is an Index in SQL? (With Example)

    ### 🔎 Analogy

    Imagine a **library** with thousands of books.  
    If there's **no index**, the librarian has to check **every book one by one** to find the one you're asking for.

    But with an **index**, the librarian can quickly look up the **title/author** in the index and go directly to the shelf.



    ### 🧪 Example Without Index

    Suppose you have this `employees` table:

    ```sql
    CREATE TABLE employees (
        emp_id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(30),
        email VARCHAR(100)
    );
    ```

    You insert 10,000 rows.

    Now you run this query:

    ```sql
    SELECT * FROM employees WHERE email = 'john.doe@example.com';
    ```

    ➡️ Without an index on `email`, the database has to **scan all 10,000 rows** — this is called a **full table scan**. It’s **slow**.



    ### 🚀 Creating an Index

    Let’s create an index on the `email` column:

    ```sql
    CREATE INDEX idx_email ON employees(email);
    ```

    Now the same query:

    ```sql
    SELECT * FROM employees WHERE email = 'john.doe@example.com';
    ```

    ➡️ This time, the **index is used**, and the database **jumps directly** to the matching row, much faster.



    ### 🧠 Behind the Scenes

    - The database creates a **data structure** (like a B-Tree) for fast lookup.
    - The index keeps the `email` values **sorted internally**, so binary search can be used instead of scanning all rows.



    ### ⚠️ Index Trade-offs

    | Pros                          | Cons                                      |
    |------------------------------|-------------------------------------------|
    | Fast SELECT and JOIN queries | Slower INSERT, UPDATE, DELETE operations  |
    | Can improve ORDER BY speed   | Takes up extra storage space              |



    ### 🔂 Composite Index Example

    You can also create an index on **multiple columns**:

    ```sql
    CREATE INDEX idx_name_dept ON employees(name, department);
    ```

    This is useful if you often query like:

    ```sql
    SELECT * FROM employees WHERE name = 'Alice' AND department = 'HR';
    ```

6. ### What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN

    ### 🔁 SQL JOIN Types Explained

    ### 1. 🧩 INNER JOIN
    - **Returns only matching rows** from both tables.
    - If there is **no match**, the row is **excluded**.
    - Most common type of join.

    ```sql
    SELECT * 
    FROM A 
    INNER JOIN B ON A.id = B.id;
    ```

    🔍 Returns only rows where `A.id = B.id`.

    ---

    ### 2. 👈 LEFT JOIN (or LEFT OUTER JOIN)
    - Returns **all rows from the left table** (A), and the **matching rows** from the right table (B).
    - If there is **no match**, result shows **NULLs** for right table’s columns.

    ```sql
    SELECT * 
    FROM A 
    LEFT JOIN B ON A.id = B.id;
    ```

    🔍 All rows from table A + matching rows from B (NULL if no match).

    ---

    ### 3. 👉 RIGHT JOIN (or RIGHT OUTER JOIN)
    - Returns **all rows from the right table** (B), and the **matching rows** from the left table (A).
    - If there is **no match**, result shows **NULLs** for left table’s columns.

    ```sql
    SELECT * 
    FROM A 
    RIGHT JOIN B ON A.id = B.id;
    ```

    🔍 All rows from table B + matching rows from A (NULL if no match).

    ---

    ### 4. 🔄 FULL OUTER JOIN
    - Returns **all rows from both tables**, with matching rows from both sides.
    - If there is **no match**, NULLs are shown for the missing side.

    ```sql
    SELECT * 
    FROM A 
    FULL OUTER JOIN B ON A.id = B.id;
    ```

    🔍 All rows from A and B; matched rows are joined, unmatched ones show NULLs.

    > ❗Note: MySQL doesn’t support `FULL OUTER JOIN` directly — use `UNION` of `LEFT JOIN` and `RIGHT JOIN` to simulate it.

    ---

    ### 📊 Summary Table

    | Join Type            | Rows from A | Rows from B | Unmatched A | Unmatched B |
    |----------------------|-------------|-------------|-------------|-------------|
    | **INNER JOIN**        | ✅           | ✅           | ❌           | ❌           |
    | **LEFT JOIN**         | ✅           | ✅           | ✅           | ❌           |
    | **RIGHT JOIN**        | ✅           | ✅           | ❌           | ✅           |
    | **FULL OUTER JOIN**   | ✅           | ✅           | ✅           | ✅           |


7. ### What is the difference between DELETE, TRUNCATE, and DROP

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



8. ### What the difference between UNION and UNION  ALL
    ### 🧾 Difference Between `UNION` and `UNION ALL` in SQL

    | Feature                | `UNION`                                                | `UNION ALL`                                           |
    |------------------------|--------------------------------------------------------|--------------------------------------------------------|
    | **Duplicate Rows**     | Removes duplicate rows from the result set.           | Includes **all rows**, even if duplicates exist.       |
    | **Performance**        | Slower, due to duplicate elimination and sorting.     | Faster, as it skips duplicate checking.                |
    | **Use Case**           | Use when you need only **unique** results.            | Use when you want to **preserve all rows**, including duplicates. |
    | **Sorting**            | Performs internal sorting to remove duplicates.       | No sorting is performed.                              |
    | **Result Size**        | Smaller, if duplicates exist.                         | Larger, as it contains all entries.                    |



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


9. ### What are the different types of joins in SQL

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


10. ### What are operators,share its type and example
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








---

## 🔹 Intermediate Level Questions


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




2. ### What is a subquery? Explain with an example

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

3. ### What is a GROUP BY clause? How is it used with aggregate functions
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


4. ### What are Aggregate Functions in SQL?

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

    #### Table: Orders

    | order_id | customer | amount |
    |----------|----------|--------|
    | 1        | Alice    | 150    |
    | 2        | Bob      | 200    |
    | 3        | Alice    | 100    |
    | 4        | Charlie  | 300    |

    ---

    ### Query:

    ```sql
    SELECT customer, SUM(amount) AS total_spent
    FROM Orders
    GROUP BY customer;
    ```
    ### Output
    | customer | total\_spent |
    | -------- | ------------ |
    | Alice    | 250          |
    | Bob      | 200          |
    | Charlie  | 300          |
        
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
    



## Advance Interview question
1. ### What are window functions? How do you use RANK(), DENSE_RANK(), ROW_NUMBER()

    ### Window Functions in SQL

    ### 🔹 What are Window Functions?

    **Window functions** perform calculations across a set of rows **related to the current row**, without collapsing the rows like aggregate functions do.

    They use the **`OVER()`** clause to define a "window" of rows.

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

    ### ✅ SQL Transactions and ACID Properties

    ---

    ### 🔹 What is a Transaction in SQL?

    A **transaction** is a sequence of one or more SQL statements executed as a single unit of work.

    - It ensures **data integrity**.
    - A transaction is either **fully completed** or **fully rolled back**.

    ---

    ### 🔸 SQL Transaction Commands

    | Command             | Purpose                                       |
    |---------------------|-----------------------------------------------|
    | `START TRANSACTION` | Begins a new transaction                      |
    | `COMMIT`            | Saves all changes made by the transaction     |
    | `ROLLBACK`          | Undoes all changes made in the transaction    |

    ---

    ### ✅ Example:

    ```sql
    START TRANSACTION;

    UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
    UPDATE accounts SET balance = balance + 1000 WHERE id = 2;

    COMMIT;
    ```



    | Property            | Description                                                                                                                                                      |
    | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **A - Atomicity**   | Ensures that **all operations** within a transaction are completed successfully. If one part fails, the entire transaction is **rolled back**.                   |
    | **C - Consistency** | Guarantees that a transaction will bring the database from one **valid state to another**, maintaining all predefined **rules, constraints, and relationships**. |
    | **I - Isolation**   | Ensures that concurrent transactions **do not interfere** with each other. Intermediate states of a transaction are **invisible** to other transactions.         |
    | **D - Durability**  | Once a transaction is **committed**, the changes are **permanent**, even in the case of system failures or crashes.                                              |



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


6. ### How does the CASE statement work in SQL
    ### ✅ CASE Statement in SQL

    The `CASE` statement allows you to perform conditional logic in SQL queries, similar to `IF-ELSE` in programming languages.

    ### 🔹 Syntax

    ```sql
    CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE resultN
    END


    ```


    ---

    ### ✅ **Step 3: Example**


    ### 🔸 Example

    ```sql
    SELECT emp_id, salary,
    CASE
        WHEN salary > 50000 THEN 'High'
        WHEN salary BETWEEN 30000 AND 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_grade
    FROM employees;
    ```


7. ### What is the purpose of ALter Command

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



8. ### What Order of Execution of SQL Clauses
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


