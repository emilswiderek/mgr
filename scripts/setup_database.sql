CREATE SCHEMA `mgr2` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci ;

CREATE TABLE `mgr2`.`spectrum` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `measure_id` INT NULL,
  `mean_rr` FLOAT NULL,
  `stdev` FLOAT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `measure_id` (`measure_id` ASC));

CREATE TABLE `mgr2`.`measure` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `measure_type` VARCHAR(255) NULL,
  `breath_period` INT NULL,
  `heart_period` INT NULL,
  `min_breath_period` INT NULL,
  `max_breath_period` INT NULL,
  `breath_number` INT NULL,
  `updated_at` TIMESTAMP NULL DEFAULT now(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

ALTER TABLE `mgr2`.`measure`
ADD INDEX `measure_type` (`measure_type` ASC),
ADD INDEX `breath_period` (`breath_period` ASC),
ADD INDEX `heart_period` (`heart_period` ASC),
ADD INDEX `min_breath_period` (`min_breath_period` ASC),
ADD INDEX `max_breath_period` (`max_breath_period` ASC);

ALTER TABLE `mgr2`.`spectrum`
ADD COLUMN `breath_period` INT NULL AFTER `stdev`;

ALTER TABLE `mgr2`.`measure`
ADD COLUMN `response_function` VARCHAR(255) NULL AFTER `updated_at`;

CREATE TABLE `mgr2`.`heartbeats` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `heart_phase` INT NOT NULL,
  `measure_id` INT NOT NULL,
  `breath_phase` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

 -- todo: after insertion:
ALTER TABLE `mgr2`.`heartbeats`
ADD INDEX `measure_id` (`measure_id` ASC),
ADD INDEX `heart_phase` (`heart_phase` ASC),
ADD INDEX `breath_phase` (`breath_phase` ASC);

CREATE
    ALGORITHM = UNDEFINED
    DEFINER = `itplement`@`localhost`
    SQL SECURITY DEFINER
VIEW `generation_results` AS
    (select
        `m`.`measure_type` AS `measure_type`,
        `m`.`breath_period` AS `breath_period`,
        `m`.`heart_period` AS `heart_period`,
        `m`.`min_breath_period` AS `min_breath_period`,
        `m`.`max_breath_period` AS `max_breath_period`,
        `m`.`breath_number` AS `breath_number`,
        `m`.`response_function` AS `response_function`,
        `h`.`id` AS `result_id`,
        `h`.`heart_phase` AS `heart_phase`,
        `h`.`measure_id` AS `measure_id`,
        `h`.`breath_phase` AS `breath_phase`
    from
        (`measure` `m`
        join `heartbeats` `h` ON ((`m`.`id` = `h`.`measure_id`)))
    where
        ((`m`.`measure_type` = 'gen_ext')
            and (`h`.`breath_phase` = 1))
    order by `h`.`id`)