```sql

CREATE DATABASE Program06;
USE Program06;

-- Create N_RollCall table
CREATE TABLE N_RollCall (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255),
    birth_date DATE
);

-- Create O_RollCall table with common data
CREATE TABLE O_RollCall (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255),
    birth_date DATE
);

-- Insert common data into O_RollCall
INSERT INTO O_RollCall (student_id, student_name, birth_date)
VALUES
    (1, 'Ram', '1995-08-15'),
    (3, 'Bheem', '1990-12-10');

-- Insert sample records into N_RollCall
INSERT INTO N_RollCall (student_id, student_name, birth_date)
VALUES
    (1, 'Ram', '1995-08-15'),  -- Common record with O_RollCall
    (2, 'Shyam', '1998-03-22'),
    (3, 'Bheem', '1990-12-10'), -- Common record with O_RollCall
    (4, 'Denise', '2000-05-18'),
    (5, 'Rehman', '1997-09-03');

-- merge_rollcall_data stored procedure
DELIMITER //

CREATE PROCEDURE merge_rollcall_data()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE n_id INT;
    DECLARE n_name VARCHAR(255);
    DECLARE n_birth_date DATE;

    -- Declare cursor for N_RollCall table
    DECLARE n_cursor CURSOR FOR
        SELECT student_id, student_name, birth_date
        FROM N_RollCall;

    -- Declare handler for cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET done = TRUE;

    -- Open the cursor
    OPEN n_cursor;

    -- Start looping through cursor results
    cursor_loop: LOOP
        -- Fetch data from cursor into variables
        FETCH n_cursor INTO n_id, n_name, n_birth_date;

        -- Check if no more rows to fetch
        IF done THEN
            LEAVE cursor_loop;
        END IF;

        -- Check if the data already exists in O_RollCall
        IF NOT EXISTS (
            SELECT 1
            FROM O_RollCall
            WHERE student_id = n_id
        ) THEN
            -- Insert the record into O_RollCall
            INSERT INTO O_RollCall (student_id, student_name, birth_date)
            VALUES (n_id, n_name, n_birth_date);
        END IF;
    END LOOP;

    -- Close the cursor
    CLOSE n_cursor;
END//

DELIMITER ;


-- execute the merge_rollcall_data stored procedure
CALL merge_rollcall_data();
-- Select all records from O_RollCall
SELECT * FROM O_RollCall;
```
