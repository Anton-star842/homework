INSERT INTO Users (Id, Email, Password, FirstName, LastName, DogName, PhotoUrl)
VALUES 
    (1, 'antonmushtin900@gmail.com', 'пароль', 'Anton', 'Mushtyn', 'Dexter', NULL);

INSERT INTO Users (Id, Email, Password, FirstName, LastName, DogName, PhotoUrl)
VALUES 
    (2, 'ihor.harahatiy@lms.com', 'securepass', 'Ihor', 'Harahatiy', NULL, NULL);

INSERT INTO Courses (Id, TeacherId, Name, Description)
VALUES 
    (1, 2, 'robot_dream', 'Курс про створення LMS для роботи з базами даних.');

INSERT INTO Course_Students (CourseId, StudentId)
VALUES 
    (1, 1);

INSERT INTO Lessons (Id, CourseId, Name, Description)
VALUES 
    (1, 1, 'LMS', 'Вступ до баз даних. Посилання на заняття: https://lms.robotdreams.cc/course/2169/lesson/39429');
INSERT INTO Lessons (Id, CourseId, Name, Description)
VALUES 
    (1, 1, 'LMS', 'Вступ до баз даних. Посилання на заняття: https://lms.robotdreams.cc/course/2169/lesson/39429');

INSERT INTO Homework (Id, CourseId, Description, MaxGrade)
VALUES 
    (1, 1, 'Вступ до баз даних. Виконати завдання з розробки LMS.', 6);

INSERT INTO Homework_Answers (Id, HomeworkId, Description, StudentId, Grade)
VALUES 
    (1, 1, 'Відповідь на завдання доступна за посиланням: https://lms.robotdreams.cc/course/2169/lesson/39429', 1, 5);
