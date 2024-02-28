--Задание 2

-- 1 название и продолжительность самого продолжительного трека;
SELECT название, длительность FROM Трэк
WHERE длительность = (SELECT MAX(длительность) FROM Трэк);

-- 2 название треков, продолжительность которых не менее 3,5 минут;
SELECT название, длительность FROM Трэк
	WHERE длительность >= '00:03:30';

-- 3 названия сборников, вышедших в период с 2018 по 2020 год с ограничениями;
SELECT * FROM Альбом
	WHERE год_выпуска BETWEEN 2018 AND 2020;

-- 4 исполнители, чье имя состоит из 1 слова;
select имя FROM Исполнитель
	WHERE имя NOT LIKE  '%% %%';
	
-- 5 название треков, которое содержит слово "мой"/"my".
SELECT название FROM Трэк
	название ~* '[ ]?\mмой\M[ ]?';

--Задание 3

-- 1 Количество исполнителей в каждом жанре.
SELECT жанр_id, COUNT(исполнитель_id) FROM Жанр_Исполнитель
GROUP BY жанр_id;

-- 2 Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(трэк_id) AS количество_трэков FROM Трэк 
JOIN Альбом ON Трэк.альбом_id = Альбом.альбом_id 
WHERE год_выпуска BETWEEN '2019' AND '2020';

-- 3 Средняя продолжительность треков по каждому альбому.
SELECT Альбом.название, AVG(Трэк.длительность) FROM Альбом 
INNER JOIN Трэк ON Альбом.альбом_id = Трэк.альбом_id
GROUP BY Альбом.название;

-- 4 Все исполнители, которые не выпустили альбомы в 2020 году
SELECT Исполнитель.имя FROM Исполнитель
WHERE NOT исполнитель_id IN(SELECT исполнитель_id FROM Исполнитель_Альбом
JOIN Альбом ON Исполнитель_Альбом.альбом_id = Альбом.альбом_id
WHERE  Альбом.год_выпуска = 2020);

-- 5 Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT Сборник.название 
FROM Сборник
JOIN Трэк_Сборник ON Сборник.сборник_id = Трэк_Сборник.сборник_id
JOIN Трэк ON Трэк_Сборник.сборник_id = Трэк.трэк_id
JOIN Альбом ON Трэк.альбом_id = Альбом.альбом_id
JOIN Исполнитель_Альбом ON Альбом.альбом_id = Исполнитель_Альбом.альбом_id
JOIN Исполнитель ON Исполнитель.исполнитель_id = Исполнитель_Альбом.исполнитель_id
WHERE Исполнитель.имя = 'Исполнитель номер 1' 
GROUP by Сборник.название
ORDER BY Сборник.название;
