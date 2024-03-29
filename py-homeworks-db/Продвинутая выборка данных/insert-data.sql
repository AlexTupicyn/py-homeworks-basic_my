--музыкальные жанры
INSERT INTO Жанр
VALUES (1, 'Жанр1'), (2,'Жанр2'), (3, 'Жанр3'), (4, 'Жанр4');

--исполнители
INSERT INTO Исполнитель
VALUES (1, 'Исполнитель номер 1'), (2, 'Исполнитель2'), (3, 'Исполнитель 3'), (4, 'Исполнитель 4');

--жанры исполнителей
INSERT INTO Жанр_Исполнитель
VALUES (1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (4, 2);

--альбомы
INSERT INTO Альбом
VALUES (1, 'Альбом1', 2011), (2, 'Альбом2', 2012), (3, 'Альбом3', 2020);

--исполнители, выпустившие альбомы
INSERT INTO Исполнитель_Альбом
VALUES (1,1), (2,2), (3,3), (1,3), (2,3), (4,2);

--треки
INSERT INTO Трэк (название, длительность, альбом_id )
VALUES ('Название трека1', '00:04:12', 1), ('Название трека2', '00:02:59', 1), 
('Название трека3 мой любимый трек', '00:05:41', 2), 
('Название трека4', '00:02:46', 2), ('Название трека5', '00:03:45', 3), 
('Название трека6', '00:02:19', 3);

--сборники
INSERT INTO Сборник(название, год_выпуска)
VALUES ('Сборник1', 2020), ('Сборник2', 2021), ('Сборник3', 2021), ('Сборник4', 2022);

--треки сборников
INSERT INTO Трэк_Сборник
VALUES (1,1), (1,3), (1,4), (2,2), (2,4), (3,1), (3,2), (3,3), (3,4), (4,1), (4,3);
