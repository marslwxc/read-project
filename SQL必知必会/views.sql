CREATE VIEW player_above_avg_height AS
SELECT player_id, height
FROM player
WHERE height > (SELECT AVG(height) FROM player);

CREATE VIEW player_above_above_avg_height AS
SELECT player_id, player_name, height
FROM player
WHERE height > (SELECT AVG(height) from player_above_avg_height);

ALTER VIEW player_above_avg_height AS
SELECT player_id, player_name, height
FROM player
WHERE height > (SELECT height > AVG(height) FROM player);

DROP VIEW player_above_above_avg_height;

CREATE VIEW player_height_grades AS
SELECT p.player_name, p.height, h.height_level
FROM player AS p JOIN height_grades AS h
ON height BETWEEN h.height_lowest AND h.height_highest;

CREATE VIEW player_team AS
SELECT CONCAT(player_name,'(',team.team_name,')') AS player_team
FROM player JOIN team
where player.team_id = team.team_id;