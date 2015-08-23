CREATE SCHEMA `mgr` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci ;

CREATE TABLE `mgr`.`spectrum` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `measure_id` INT NULL,
  `mean_rr` FLOAT NULL,
  `stdev` FLOAT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `measure_id` (`measure_id` ASC));

CREATE TABLE `mgr`.`measure` (
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

ALTER TABLE `mgr`.`measure`
ADD INDEX `measure_type` (`measure_type` ASC),
ADD INDEX `breath_period` (`breath_period` ASC),
ADD INDEX `heart_period` (`heart_period` ASC),
ADD INDEX `min_breath_period` (`min_breath_period` ASC),
ADD INDEX `max_breath_period` (`max_breath_period` ASC);

ALTER TABLE `mgr`.`spectrum`
ADD COLUMN `breath_period` INT NULL AFTER `stdev`;

ALTER TABLE `mgr`.`measure`
ADD COLUMN `response_function` VARCHAR(255) NULL AFTER `updated_at`;

CREATE TABLE `mgr`.`heartbeats` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `heart_phase` INT NOT NULL,
  `measure_id` INT NOT NULL,
  `breath_phase` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));


ALTER TABLE `mgr`.`heartbeats`
ADD INDEX `measure_id` (`measure_id` ASC);
ADD INDEX `heart_phase` (`heart_phase` ASC),
ADD INDEX `breath_phase` (`breath_phase` ASC);

