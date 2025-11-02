CREATE DATABASE pyproject;
USE pyproject;
-- CREATING TABLE FOR DATA --
CREATE TABLE Students (
    NAME_OF_THE_STUDENT VARCHAR(30),
    UNIVERSITY VARCHAR(50),
    PROGRAM_NAME VARCHAR(50),
    Specialisation VARCHAR(100),
    Domain VARCHAR(50),
    GENERAL_MANAGEMENT_SCORE INT NOT NULL,
    DOMAIN_SPECIFIC_SCORE INT NOT NULL,
    TOTAL_SCORE INT NOT NULL,
    LOGIN_IDS VARCHAR(15)
);
-- ADD DATA --
INSERT INTO Students VALUES ('Camila Wood', 'Stanford University, USA', 'B.Com', 'Honours', 'Finance', 50, 50, 100, 'STFBCM001');
INSERT INTO Students VALUES ('Liam Taylor', 'Harvard University, USA', 'B.Com', 'Accounting Analytics', 'BA', 50, 50, 100, 'HRVBCM001');
INSERT INTO Students VALUES ('Emily King', 'University of Cambridge, UK', 'MBA', 'Data Analytics', 'DA', 50, 50, 100, 'CAMMBA003');
INSERT INTO Students VALUES ('Lucas Evans', 'University of Oxford, UK', 'Intg. BBAMBA', 'Financial Services', 'Finance', 49, 47, 96, 'OXFIB001');
INSERT INTO Students VALUES ('Madison Davis', 'Massachusetts Institute of Technology MIT, USA', 'BBA', 'Digital Marketing', 'DM', 45, 39, 84, 'MASBBA001');
INSERT INTO Students VALUES ('Scarlett Cooper','Stanford University, USA','BBA','International Business','IB',49,43,92,'STFBBA008');
INSERT INTO Students VALUES ('Gabriel Wilson', 'Imperial College London, UK', 'BBA', 'Entrepreneurship Innovation', 'EI', 33, 33, 66, 'ICLBBA001');
INSERT INTO Students VALUES ('Liam Taylor','Harvard University, USA','MBA','Innovation Entrepreneurship and Venture Development','E&I',37,25,62,'HRVMBA058');
INSERT INTO Students VALUES ('Ella Stewart', 'Stanford University, USA', 'BBA', 'International Business', 'IB', 41, 16, 57, 'STFBBA041');
INSERT INTO Students VALUES ('Layla Jackson','Harvard University, USA','MBA','International Business','IB',28,33,61,'HRVMBA061');
INSERT INTO Students VALUES ('Aiden Thompson', 'University of Oxford, UK', 'Intg. BBAMBA', 'Financial Services', 'Finance', 21, 9, 30, 'OXFIB012');
INSERT INTO Students VALUES ('Logan Brown','University of Oxford, UK','Intg. BBA+MBA','Financial Services','Finance',28,20,48,'OXFIB010');
INSERT INTO Students VALUES ('Emily Lee', 'Massachusetts Institute of Technology MIT, USA', 'BBA', 'Digital Marketing', 'DM', 4, 1, 5, 'MASBBA009');
INSERT INTO Students VALUES ('Aria King', 'University of Cambridge, UK', 'BBA', 'International Business', 'Finance', 15, 15, 30, 'CAMBBA002');
INSERT INTO Students VALUES ('Samuel Perez', 'Stanford University, USA', 'BBA', 'International Business', 'IB', 12, 8, 20, 'STFBBA050');
SELECT * FROM Students;
-- FILTERING --
SELECT NAME_OF_THE_STUDENT,LOGIN_IDS FROM Students WHERE GENERAL_MANAGEMENT_SCORE > 20 AND DOMAIN_SPECIFIC_SCORE <20 AND TOTAL_SCORE>50;
SELECT NAME_OF_THE_STUDENT,LOGIN_IDS FROM Students WHERE PROGRAM_NAME ='MBA' AND DOMAIN = 'Finance';
SELECT * FROM Students WHERE NAME_OF_THE_STUDENT ='Liam Taylor';
-- CREATION  --
ALTER TABLE Students ADD COLUMN Remarks VARCHAR(100);   
-- UPDATE --
UPDATE Students SET Remarks='Execellent' WHERE TOTAL_SCORE>90;
UPDATE Students SET Remarks='Good' WHERE 89<TOTAL_SCORE<40;
UPDATE Students SET Remarks='Needs Improvement' WHERE TOTAL_SCORE<39;
-- DELETING --
ALTER TABLE Students DROP COLUMN Domain;
DELETE FROM Students WHERE TOTAL_SCORE<40;
-- UPDATE EXISTING DATA --
UPDATE Students SET PROGRAM_NAME='M.Com' WHERE PROGRAM_NAME='B.Com';
UPDATE Students SET Specialisation='Ph.D' WHERE Specialisation='Honours';
UPDATE Students SET TOTAL_SCORE =40 WHERE TOTAL_SCORE<40;
SET SQL_SAFE_UPDATES=0;
