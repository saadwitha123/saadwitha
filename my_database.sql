CREATE DATABASE university;
USE uviversity;
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);
INSERT INTO Students (id, name, age, grade)
VALUES (1, 'Rahul', 15, '10th');
INSERT INTO Students (id, name, age, grade)
VALUES
(2, 'Sneha', 16, '11th'),
(3, 'Riya', 17, '12th');
SELECT * FROM Students;
