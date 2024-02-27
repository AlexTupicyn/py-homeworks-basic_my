CREATE TABLE IF NOT EXISTS Жанр (
	жанр_ID SERIAL PRIMARY KEY,
	название VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Исполнитель (
	исполнитель_ID SERIAL PRIMARY KEY,
	имя VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Жанр_Исполнитель (
	жанр_ID INT REFERENCES Жанр(жанр_ID),
	исполнитель_ID INT REFERENCES Исполнитель(исполнитель_ID),
	CONSTRAINT pk1 PRIMARY KEY (жанр_ID, исполнитель_ID)
);

CREATE TABLE IF NOT EXISTS Альбом (
	альбом_ID SERIAL PRIMARY KEY,
	название VARCHAR(60) NOT NULL,
	год_выпуска INT NOT NULL 
);

CREATE TABLE IF NOT EXISTS Исполнитель_Альбом (
	исполнитель_ID INT REFERENCES Исполнитель(исполнитель_ID),
	альбом_ID INT REFERENCES Альбом(альбом_ID),
	CONSTRAINT pk2 PRIMARY KEY (исполнитель_ID, альбом_ID)
);

CREATE TABLE IF NOT EXISTS Трэк (
	трэк_ID SERIAL PRIMARY KEY,
	название VARCHAR(60) NOT NULL,
	год_выпуска INTEGER NOT NULL,
	альбом_ID INTEGER REFERENCES Альбом(альбом_ID)
);

CREATE TABLE IF NOT EXISTS  Сборник (
	сборник_ID SERIAL PRIMARY KEY,
	название VARCHAR(60) NOT NULL,
	год_выпуска INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS  Трэк_Сборник (
	трэк_ID INT REFERENCES Трэк(трэк_ID),
	сборник_ID INT REFERENCES Сборник(сборник_ID),
	CONSTRAINT pk3 PRIMARY KEY (трэк_ID, сборник_ID)
);

