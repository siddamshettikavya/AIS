CREATE TABLE staff (
    emp_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    department VARCHAR2(50),
    salary NUMBER,
    hire_date DATE
);
INSERT ALL
    INTO staff (emp_id, first_name, last_name, department, salary, hire_date) VALUES (1, 'Amit',  'Sharma',   'HR',        45000, DATE '2020-05-20')
    INTO staff (emp_id, first_name, last_name, department, salary, hire_date) VALUES (2, 'Priya', 'Patel',    'Finance',   60000, DATE '2021-02-10')
    INTO staff (emp_id, first_name, last_name, department, salary, hire_date) VALUES (3, 'Ravi',  'Kumar',    'IT',        55000, DATE '2019-08-14')
    INTO staff (emp_id, first_name, last_name, department, salary, hire_date) VALUES (4, 'Neha',  'Reddy',    'Marketing', 48000, DATE '2022-01-05')
    INTO staff (emp_id, first_name, last_name, department, salary, hire_date) VALUES (5, 'Arjun', 'Singh',    'IT',        62000, DATE '2020-09-12')
SELECT * FROM dual;
COMMIT;
select * from staff;
SELECT first_name, last_name, department FROM staff;
SELECT DISTINCT department FROM staff;
SELECT * FROM staff WHERE salary > 5000;
SELECT * FROM staff WHERE department = 'IT';
