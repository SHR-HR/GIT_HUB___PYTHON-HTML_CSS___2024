-- CREATE TABLE Students (
--     StudentID SERIAL PRIMARY KEY,
--     StudentName VARCHAR(50)
-- );

-- CREATE TABLE Courses (
--     CourseID SERIAL PRIMARY KEY,
--     CourseName VARCHAR(50)
-- );

-- ALTER TABLE Students
-- ADD COLUMN CourseID INT,
-- ADD CONSTRAINT fk_course
--     FOREIGN KEY (CourseID)
--     REFERENCES Courses(CourseID);

-- CREATE TABLE Authors (
--     AuthorID SERIAL PRIMARY KEY,
--     AuthorName VARCHAR(50)
-- );

-- CREATE TABLE Books (
--     BookID SERIAL PRIMARY KEY,
--     BookName VARCHAR(100),
--     AuthorID INT,
--     CONSTRAINT fk_author
--         FOREIGN KEY (AuthorID)
--         REFERENCES Authors(AuthorID)
--         ON DELETE CASCADE
-- );

-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'public';

-- SELECT
--     tc.constraint_name,
--     tc.table_name,
--     kcu.column_name,
--     ccu.table_name AS foreign_table_name,
--     ccu.column_name AS foreign_column_name
-- FROM
--     information_schema.table_constraints AS tc
--     JOIN information_schema.key_column_usage AS kcu
--       ON tc.constraint_name = kcu.constraint_name
--     JOIN information_schema.constraint_column_usage AS ccu
--       ON ccu.constraint_name = tc.constraint_name
-- WHERE constraint_type = 'FOREIGN KEY';

-- SELECT * FROM Students;
-- SELECT * FROM Courses;
-- SELECT * FROM Authors;
-- SELECT * FROM Books;

-- DO $$ DECLARE
--     r RECORD;
-- BEGIN
--     FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
--         EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
--     END LOOP;
-- END $$;









-- CREATE TABLE Courses (
--     CourseID SERIAL PRIMARY KEY,
--     CourseName VARCHAR(50)
-- );

-- CREATE TABLE Students (
--     StudentID SERIAL PRIMARY KEY,
--     StudentName VARCHAR(50),
--     CourseID INT REFERENCES Courses(CourseID)
-- );

-- CREATE TABLE Authors (
--     AuthorID SERIAL PRIMARY KEY,
--     AuthorName VARCHAR(50)
-- );

-- CREATE TABLE Books (
--     BookID SERIAL PRIMARY KEY,
--     BookName VARCHAR(100),
--     AuthorID INT REFERENCES Authors(AuthorID) ON DELETE CASCADE -- Создаем внешний ключ с каскадным удалением
-- );


-- SELECT column_name, data_type
-- FROM information_schema.columns
-- WHERE table_name = 'Authors';


-- SELECT column_name, data_type
-- FROM information_schema.columns
-- WHERE table_name = 'Books';


-- SELECT
--     tc.constraint_name,
--     tc.table_name,
--     kcu.column_name,
--     ccu.table_name AS foreign_table_name,
--     ccu.column_name AS foreign_column_name
-- FROM
--     information_schema.table_constraints AS tc
--     JOIN information_schema.key_column_usage AS kcu
--       ON tc.constraint_name = kcu.constraint_name
--     JOIN information_schema.constraint_column_usage AS ccu
--       ON ccu.constraint_name = tc.constraint_name
-- WHERE 
--     tc.table_name = 'Books' AND
--     tc.constraint_type = 'FOREIGN KEY';


-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'public';

-- SELECT
--     tc.constraint_name,
--     tc.table_name,
--     kcu.column_name,
--     ccu.table_name AS foreign_table_name,
--     ccu.column_name AS foreign_column_name
-- FROM
--     information_schema.table_constraints AS tc
--     JOIN information_schema.key_column_usage AS kcu
--       ON tc.constraint_name = kcu.constraint_name
--     JOIN information_schema.constraint_column_usage AS ccu
--       ON ccu.constraint_name = tc.constraint_name
-- WHERE constraint_type = 'FOREIGN KEY';

