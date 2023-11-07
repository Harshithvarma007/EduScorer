-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS evaluation_db;

-- Use the database
USE evaluation_db;

-- Create the 'questions' table to store questions
CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT NOT NULL,
    solution TEXT NOT NULL DEFAULT 'No solution provided',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'teachers' table to store teacher information
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'students' table to store student information
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'evaluation' table to store evaluation information
CREATE TABLE evaluation (
    evaluation_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    student_id INT NOT NULL,
    teacher_id INT NOT NULL,
    marks INT,
    accuracy DECIMAL(5, 2),
    completeness DECIMAL(5, 2),
    length DECIMAL(5, 2),
    relevance DECIMAL(5, 2),
    clarity DECIMAL(5, 2),
    evaluation_comment TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES questions (question_id),
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
);

-- Create the 'answers' table to store student answers
CREATE TABLE answers (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    evaluation_id INT NOT NULL,
    answer_text TEXT NOT NULL,
    explanation TEXT,
    FOREIGN KEY (evaluation_id) REFERENCES evaluation (evaluation_id)
);

-- Create a 'corrections' table to track corrections
CREATE TABLE corrections (
    correction_id INT AUTO_INCREMENT PRIMARY KEY,
    evaluation_id INT NOT NULL,
    teacher_id INT NOT NULL,
    correction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evaluation_id) REFERENCES evaluation (evaluation_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
);
