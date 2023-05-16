CREATE TABLE `produtos` (
	`id` INT(10) NOT NULL,
	`produto` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`preco` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`marca` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_0900_ai_ci'
)
COLLATE='utf8mb4_0900_ai_ci'
ENGINE=InnoDB
;
