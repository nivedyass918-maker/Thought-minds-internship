CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0)
);
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL
);
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Students(student_id),
    course_id INT REFERENCES Courses(course_id),
    enrollment_date DATE DEFAULT CURRENT_DATE
);
INSERT INTO Students (student_name, age)
VALUES
('Alaina', 20),
('Rahul', 21),
('Anu', 19);
INSERT INTO Courses (course_name, credits)
VALUES
('Python', 4),
('SQL', 3),
('Java', 4);
INSERT INTO Enrollments (student_id, course_id)
VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 1);
SELECT * FROM Students;
SELECT * FROM Courses;
SELECT s.student_name,
       c.course_name
FROM Enrollments e
JOIN Students s ON e.student_id = s.student_id
JOIN Courses c ON e.course_id = c.course_id;
SELECT COUNT(*) FROM Students;
SELECT * FROM Students
ORDER BY age;
CREATE INDEX idx_student_name
ON Students(student_name);
SELECT e.enrollment_id,
       s.student_name,
       c.course_name,
       e.enrollment_date
FROM Enrollments e
JOIN Students s ON e.student_id = s.student_id
JOIN Courses c ON e.course_id = c.course_id;

