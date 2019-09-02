# DECLARE cursor_name CURSOR FOR select_statement
# DECLARE cursor_name CURSOR 
# FOR
# SELECT hp_max 
# FROM heros;
# OPEN cursor_name
# FETCH cursor_name INTO var_name
# CLOSE cursor_name

DROP PROCEDURE calc_hp_max;
CREATE PROCEDURE calc_hp_max()
BEGIN
	DECLARE hp INT;

	DECLARE hp_sum INT DEFAULT 0;
	DECLARE done INT DEFAULT false;
	DECLARE cur_hero CURSOR FOR SELECT hp_max FROM heros;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = true;

	OPEN cur_hero;
	read_loop:LOOP
	FETCH cur_hero INTO hp;
	IF done THEN 
		LEAVE read_loop;
	END IF;
	SET hp_sum = hp_sum + hp;
	END LOOP;
	CLOSE cur_hero;
	SELECT hp_sum;
END

CALL calc_hp_max();

CREATE PROCEDURE alter_attack_growth()
BEGIN
	-- 创建接收游标的变量
	DECLARE temp_id INT;
	DECLARE temp_growth, temp_max, temp_start, temp_diff FLOAT;
	-- 创建结束标志变量
	DECLARE done INT DEFAULT false;
	-- 定义游标
	DECLARE cur_hero CURSOR FOR SELECT id, attack_growth, attack_max, attack_start FROM heros;
	-- 指定游标循环结束时的返回值
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = true;
	
	OPEN cur_hero;
	FETCH cur_hero INTO temp_id, temp_growth, temp_max, temp_start;
	REPEAT
		IF NOT done THEN
			SET temp_diff = temp_max - temp_start;
			IF temp_growth < 5 THEN
				IF temp_diff > 200 THEN
					SET temp_growth = temp_growth * 1.1;
				ELSEIF temp_diff >= 150 AND temp_diff <= 200 THEN
					SET temp_growth = temp_growth * 1.08;
				ELSEIF temp_diff < 150 THEN
					SET temp_growth = temp_growth * 1.07;
				END IF;
			ELSEIF temp_growth >= 5 and temp_growth <= 10 THEN
				SET temp_growth = temp_growth * 1.05;
			END IF;
			UPDATE heros SET attack_growth = ROUND(temp_growth, 3) WHERE id = temp_id;
		END IF;
	FETCH cur_hero INTO temp_id, temp_growth, temp_max, temp_start;
	UNTIL done = TRUE END REPEAT;

	CLOSE cur_hero;
END

CALL alter_attack_growth();

SELECT heros.id, heros.attack_growth FROM heros;