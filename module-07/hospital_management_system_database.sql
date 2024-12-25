-- Create database
CREATE DATABASE hospital_db;

-- Create Departments Table
CREATE Table departments(
 department_id BIGINT (20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(50) NOT NULL,
 location VARCHAR(100) NOT NULL,
 created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
 updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
);

-- Create Doctors Table
CREATE Table doctors (
    doctor_id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department_id BIGINT(20) UNSIGNED NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Create Patients Table
CREATE Table patients (
    patient_id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age int(5) NOT NULL,
    gender VARCHAR(15) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()

);

-- Create Appointments Table
CREATE Table appointments (
    appointment_id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    status VARCHAR(20) NOT NULL, 
    patient_id BIGINT(20) UNSIGNED NOT NULL, 
    doctor_id BIGINT(20) UNSIGNED NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE RESTRICT ON UPDATE CASCADE
);



------------------------------------ query----------------------------
-- Insert Dummy Data into Departments
INSERT INTO departments (name, location) VALUES
('Cardiology', '1st Floor'),
('Neurology', '2nd Floor'),
('Pediatrics', '3rd Floor'),
('Orthopedics', '4th Floor'),
('Dermatology', '5th Floor');

-- Insert Dummy Data into Doctors
INSERT INTO doctors (name, specialization, phone, department_id) VALUES
('Dr. John Doe', 'Cardiologist', '1234567890', 1),
('Dr. Jane Smith', 'Neurologist', '2345678901', 2),
('Dr. Mike Brown', 'Pediatrician', '3456789012', 3),
('Dr. Anna White', 'Orthopedic Surgeon', '4567890123', 4),
('Dr. Sarah Green', 'Dermatologist', '5678901234', 5);

-- Insert Dummy Data into Patients
INSERT INTO patients (name, age, gender, phone) VALUES
('Alice Johnson', 29, 'Female', '9876543210'),
('Bob Williams', 45, 'Male', '8765432109'),
('Charlie Davis', 12, 'Male', '7654321098'),
('Daisy Miller', 35, 'Female', '6543210987'),
('Evan Harris', 60, 'Male', '5432109876');

-- Insert Dummy Data into Appointments
INSERT INTO appointments (date, time, status, patient_id, doctor_id) VALUES
('2024-12-21', '10:00:00', 'Scheduled', 1, 1),
('2024-12-22', '11:00:00', 'Completed', 2, 2),
('2024-12-23', '12:00:00', 'Scheduled', 3, 3),
('2024-12-24', '13:00:00', 'Cancelled', 4, 4),
('2024-12-25', '14:00:00', 'Scheduled', 5, 5);



