CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    dog_name VARCHAR(100),
    photo BLOB
);

CREATE TABLE Courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (teacher_id) REFERENCES Users(id)
);

CREATE TABLE Course_Students (
    course_id INT NOT NULL,
    student_id INT NOT NULL,
    PRIMARY KEY (course_id, student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(id),
    FOREIGN KEY (student_id) REFERENCES Users(id)
);

CREATE TABLE Lessons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

CREATE TABLE Assignments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT NOT NULL,
    description TEXT,
    max_grade INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

CREATE TABLE Assignment_Responses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    assignment_id INT NOT NULL,
    student_id INT NOT NULL,
    response TEXT,
    grade INT,
    FOREIGN KEY (assignment_id) REFERENCES Assignments(id),
    FOREIGN KEY (student_id) REFERENCES Users(id)
);
