CREATE DATABASE testing;
USE testing;

CREATE TABLE Occultation (
    ID      int NOT NULL AUTO_INCREMENT,
    radius  int,
    imaxrr  int,
    PRIMARY KEY(ID)
);

INSERT INTO Occultation (radius)
VALUES
    (1), (2), (3), (4), (5), (6);

/* Create loop: 
where id = 1, insert 122
where id = 2, insert 123
where id = 3, insert 124
*/

/* DO THIS IN PYTHON PROGRAM, MAKE LOOP */
UPDATE Occultation
SET imaxrr = 122
WHERE ID = 1;

UPDATE Occultation
SET imaxrr = 123
WHERE ID = 2;

UPDATE Occultation
SET imaxrr = 124
WHERE ID = 3;


/*
INSERT INTO Occultation (imaxrr)
VALUES
    (122), (123), (124);
*/

DELETE FROM Occultation;  /* clear values in table */
DROP TABLE Occultation; /* delete entire table */



SELECT * FROM Occultation;

SELECT COUNT(NOT NULL imaxrr) as imaxrrs
FROM Occultation