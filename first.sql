
DROP TABLE IF EXISTS player;


CREATE TABLE player (
    id SERIAL PRIMARY KEY, 
    level INT NOT NULL,
    name VARCHAR(100),
    power INT NOT NULL,
    rank VARCHAR(50) DEFAULT 'chuttad',
    hour_played INT NOT NULL
);


INSERT INTO player (level, name, power, hour_played, rank)
VALUES 
(15, 'vishu', 4200, 12, 'chuttad'),
(88, 'rathore', 95000, 450, 'monarch'),
(42, 'kallu kaliya', 22000, 110, 'diamond II'),
(5, 'ram rahim', 450, 2, 'chuttad'),
(61, 'modiji dilfire ashique', 54000, 280, 'platinum I'),
(12, 'rahul gandhi', 2100, 8, 'chuttad'),
(75, 'lally yadav', 71000, 390, 'Immortal'),
(23, 'kejri bal', 9800, 45, 'Silver III'),
(3, 'choota hathi', 150, 1, 'chuttad'),
(50, 'kankhajura', 38000, 195, 'Gold III');

-- 3. View the final result
SELECT * FROM player
ORDER by id DESC;


--4. conditional query
SELECT name , level rank from player 
where power > 50000 
ORDER BY level DESC;


--5 update query
update player
set level = level + 22
where name = 'rathore';

--6. delete query
delete from player 
where hour_played < 10;

--7 multied query 
SELECT name, level, power, rank 
FROM player 
WHERE level > 45 OR rank = 'chuttad';


--8 aggregate function
SELECT AVG(level) as average_level, COUNT(*) as total_players
FROM player;



--9 hard query
SELECT rank, 
       COUNT(*) AS total_players_in_rank, 
       ROUND(AVG(power), 2) AS average_power
FROM player
GROUP BY rank
HAVING AVG(power) > 3000
ORDER BY average_power DESC;

SELECT name, LENGTH(name) AS name_length, rank 
FROM player
WHERE LENGTH(name) > 6 
  AND (LOWER(rank) LIKE '%platinum%' OR LOWER(rank) LIKE '%diamond%');