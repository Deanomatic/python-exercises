DELETE FROM Toy;
DELETE FROM Child;
DELETE FROM ChildToy;

DROP TABLE IF EXISTS Toy;
DROP TABLE IF EXISTS Child;
DROP TABLE IF EXISTS ChildToy;

CREATE TABLE Child (
    ChildId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Happy INT NOT NULL
);

CREATE TABLE Toy (
    ToyId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

CREATE TABLE ChildToy (
    ChildToyId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ChildId INTEGER NOT NULL,
    ToyId INTEGER NOT NULL,
    FOREIGN KEY (ChildId) REFERENCES Child(ChildId),
    FOREIGN KEY (ToyId) REFERENCES Toy(ToyId)
);



-- Toy Inserts
INSERT INTO Toy VALUES (null, 'Slime');
INSERT INTO Toy VALUES (null, 'Silly Putty');
INSERT INTO Toy VALUES (null, "He Man");

INSERT INTO Toy ('Name') VALUES ('Kite');

-- Child Inserts
INSERT INTO Child VALUES (null, "Will", 0);
INSERT INTO Child VALUES(null, 'Vincent', 0);
INSERT INTO Child VALUES(null, 'Mikey', 0);

-- ChildToy
INSERT INTO ChildToy VALUES(null, 1, 1);
INSERT INTO ChildToy VALUES(null, 1, 2);
INSERT INTO ChildToy VALUES(null, 1, 2);
INSERT INTO ChildToy VALUES(null, 4, 2);



-- Queries
SELECT * FROM Toy;
SELECT * FROM Child;
SELECT * FROM ChildToy;


SELECT c.Name, t.Name
FROM Child c, Toy t, ChildToy ct
WHERE c.ChildId = ct.ChildId
AND ct.ToyId = 4
AND c.Name = 'Mikey';


SELECT COUNT(Child.Name) NumberOfChildren
FROM Child, ChildToy, Toy
WHERE Toy.Name = 'Baseball'
AND Child.ChildId = ChildToy.ChildId
AND Toy.ToyId = ChildToy.ToyId;