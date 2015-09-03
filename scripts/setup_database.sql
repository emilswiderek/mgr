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
ADD INDEX `heart_phase` (`heart_phase` ASC);
-- ADD INDEX `breath_phase` (`breath_phase` ASC);

CREATE VIEW `generation_results` AS (
	SELECT
		h.*,
		m.breath_number,
		m.breath_period,
		m.heart_period,
		m.response_function,
		m.min_breath_period,
		m.max_breath_period
	FROM
		mgr2.heartbeats h
		left join mgr2.measure m on m.id = h.measure_id
	order by
		h.id ASC
)

