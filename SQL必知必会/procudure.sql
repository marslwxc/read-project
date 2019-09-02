CREATE PROCEDURE add_num(IN n INT)
BEGIN
	DECLARE i INT;
	DECLARE sum INT;

	SET i = 1;
	SET sum = 0;
	WHILE i <= n DO
		SET sum = sum + i;
		SET i = i + 1;
	END WHILE;
	SELECT sum;
END

CALL add_num(50)

DROP PROCEDURE get_hero_scores;
CREATE PROCEDURE get_hero_scores(
	OUT max_max_hp FLOAT,
	out min_max_mp FLOAT,
	out avg_max_attack FLOAT,
	s VARCHAR(255)
)
BEGIN
	SELECT MAX(hp_max), MIN(mp_max), AVG(attack_max)
	FROM heros
	WHERE role_main = s 
	INTO max_max_hp, min_max_mp, avg_max_attack;
END

CALL get_hero_scores(@max_max_hp, @min_max_mp, @avg_max_attack, '战士');
SELECT @max_max_hp, @min_max_mp, @avg_max_attack;

CREATE PROCEDURE get_sum_score(
	OUT sum_max_hp FLOAT,
	s VARCHAR(255)
)
BEGIN
	SELECT SUM(hp_max)
	FROM heros
	WHERE role_main = s
	INTO sum_max_hp;
END

CALL get_sum_score(@sum_max_hp, '战士');
SELECT @sum_max_hp;