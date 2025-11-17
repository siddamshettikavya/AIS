-- Hospital Billing example: create tables, insert sample data, compute totals.
-- Fixed syntax errors and made FK-friendly defaults (InnoDB). Remove the stray ")" after the Patients insert.

-- 1. Create Tables (use InnoDB so foreign keys work)
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS Services (
    service_id INT PRIMARY KEY,
    description VARCHAR(100),
    cost DECIMAL(10,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS Bills (
    bill_id INT PRIMARY KEY,
    patient_id INT,
    service_id INT,
    quantity INT,
    CONSTRAINT fk_bills_patient FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    CONSTRAINT fk_bills_service FOREIGN KEY (service_id) REFERENCES Services(service_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Insert Sample Data (no stray parentheses)
INSERT INTO Patients (patient_id, name, age, gender) VALUES
(1, 'Alice', 30, 'Female'),
(2, 'Bob', 45, 'Male'),
(3, 'Charlie', 28, 'Male');

select * FROM Patients;

INSERT INTO Services (service_id, description, cost) VALUES
(101, 'X-Ray', 500.00),
(102, 'Blood Test', 300.00),
(103, 'MRI Scan', 2500.00),
(104, 'Consultation', 700.00);

INSERT INTO Bills (bill_id, patient_id, service_id, quantity) VALUES
(1001, 1, 101, 1),  -- Alice: 1 X-Ray
(1002, 1, 104, 2),  -- Alice: 2 Consultations
(1003, 2, 102, 3),  -- Bob: 3 Blood Tests
(1004, 2, 103, 1),  -- Bob: 1 MRI Scan
(1005, 3, 104, 1);  -- Charlie: 1 Consultation

-- 3. Calculate Total Bill per Patient
SELECT 
    p.name AS patient_name,
    SUM(s.cost * b.quantity) AS total_bill
FROM 
    Patients p
JOIN 
    Bills b ON p.patient_id = b.patient_id
JOIN 
    Services s ON b.service_id = s.service_id
GROUP BY 
    p.name;
-- IMPORTANT: make sure you're using the correct database/schema before running this script.
-- Replace `your_database` with the name of your database and run: USE your_database;

-- Create (or replace) a view that holds total bill per patient so it exists before we SELECT from it
CREATE OR REPLACE VIEW PatientTotals AS
SELECT
    p.patient_id,
    p.name AS patient_name,
    SUM(s.cost * b.quantity) AS total_bill
FROM Patients p
JOIN Bills b USING (patient_id)
JOIN Services s USING (service_id)
GROUP BY p.patient_id, p.name;

SELECT * FROM PatientTotals;

-- (Tip) If you run this script from a client that opens in the `mysql` system schema, make sure to run:
-- USE your_database;   -- replace with your schema name
-- Then re-run the script or the SELECT statements below.

SHOW CREATE TABLE Patients\G
SHOW CREATE TABLE Bills\G
SELECT * FROM Patients;
SELECT * FROM Services;
SELECT * FROM Bills;
-- create a view that holds total bill per patient (used by later SELECTs)
CREATE OR REPLACE VIEW PatientTotals AS
SELECT
    p.patient_id,
    p.name AS patient_name,
    SUM(s.cost * b.quantity) AS total_bill
FROM Patients p
JOIN Bills b USING (patient_id)
JOIN Services s USING (service_id)
GROUP BY p.patient_id, p.name;

SELECT * FROM PatientTotals;

-- services used by more than one distinct patient
SELECT
    s.service_id,
    s.description,
    COUNT(DISTINCT b.patient_id) AS patient_count
FROM Services s
JOIN Bills b ON s.service_id = b.service_id
GROUP BY s.service_id, s.description
HAVING patient_count > 1;

-- services common to two specific patients (replace 1 and 2 with desired patient_id values)
SELECT
    s.service_id,
    s.description
FROM Bills b
JOIN Services s ON b.service_id = s.service_id
WHERE b.patient_id IN (1, 2)
GROUP BY s.service_id, s.description
HAVING COUNT(DISTINCT b.patient_id) = 2;

SHOW TABLE STATUS WHERE Name IN ('Patients','Services','Bills');
ALTER TABLE Patients ENGINE=InnoDB;
ALTER TABLE Services ENGINE=InnoDB;
ALTER TABLE Bills ENGINE=InnoDB;


