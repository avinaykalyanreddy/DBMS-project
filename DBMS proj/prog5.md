```sql
CREATE DATABASE Program05;
USE Program05;

CREATE TABLE Employee (
    E_id INT,
    E_name VARCHAR(255),
    Age INT,
    Salary DECIMAL(10, 2)
);

INSERT INTO Employee (E_id, E_name, Age, Salary)
VALUES
    (1, 'Ram', 30, 50000.00),
    (2, 'Bheem', 25, 45000.00),
    (3, 'Shyam', 35, 62000.00),
    (4, 'Dennis', 28, 52000.00),
    (5, 'Rehman', 32, 58000.00);
DELIMITER //

CREATE PROCEDURE fetch_employee_data()
BEGIN
    -- Declare variables to store cursor values
    DECLARE emp_id INT;
    DECLARE emp_name VARCHAR(255);
    DECLARE emp_age INT;
    DECLARE emp_salary DECIMAL(10, 2);
    
    -- Declare a cursor for the Employee table
    DECLARE emp_cursor CURSOR FOR
        SELECT E_id, E_name, Age, Salary
        FROM Employee;
    
    -- Declare a continue handler for the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET @finished = 1;
    
    -- Open the cursor
    OPEN emp_cursor;
    
    -- Initialize a variable to control cursor loop
    SET @finished = 0;
    
    -- Loop through the cursor results
    cursor_loop: LOOP
        -- Fetch the next row from the cursor into variables
        FETCH emp_cursor INTO emp_id, emp_name, emp_age, emp_salary;
        
        -- Check if no more rows to fetch
        IF @finished = 1 THEN
            LEAVE cursor_loop;
        END IF;
        
        -- Output or process each row (for demonstration, print the values)
        SELECT CONCAT('Employee ID: ', emp_id, ', Name: ', emp_name, ', Age: ', emp_age, ', Salary: ', emp_salary) AS Employee_Info;
        
    END LOOP;
    
    -- Close the cursor
    CLOSE emp_cursor;
END//

DELIMITER ;
CALL fetch_employee_data();


```
