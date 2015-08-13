CREATE SCHEMA `mgr` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci ;

CREATE TABLE `mgr`.`specrum` (
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
