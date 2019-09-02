DROP TABLE IF EXISTS `players`;

CREATE TABLE `players` (
	`player_id` INT (11) NOT NULL AUTO_INCREMENT,
	`team_id` INT (11) NOT NULL,
	`player_name` VARCHAR (255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
	`height` FLOAT (3, 2) NULL DEFAULT 0.00,
	UNIQUE INDEX (`player_name`),
	PRIMARY KEY (`player_id`) USING BTREE
) ENGINE = INNODB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

ALTER TABLE players ADD (age INT(11));
ALTER TABLE players RENAME COLUMN age to player_age;
ALTER TABLE players MODIFY player_age FLOAT(3, 1);
ALTER TABLE players DROP COLUMN player_age;

COMMIT;