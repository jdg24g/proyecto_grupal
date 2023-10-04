-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema grupal_project
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `grupal_project` ;

-- -----------------------------------------------------
-- Schema grupal_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `grupal_project` DEFAULT CHARACTER SET utf8 ;
USE `grupal_project` ;

-- -----------------------------------------------------
-- Table `grupal_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grupal_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_lvl` INT UNSIGNED NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `udapted_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grupal_project`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grupal_project`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(255) NULL,
  `price` INT UNSIGNED NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grupal_project`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grupal_project`.`cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grupal_project`.`sucursal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grupal_project`.`sucursal` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `city_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sucursal_cities_idx` (`city_id` ASC) VISIBLE,
  CONSTRAINT `fk_sucursal_cities`
    FOREIGN KEY (`city_id`)
    REFERENCES `grupal_project`.`cities` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grupal_project`.`stock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grupal_project`.`stock` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `products_id` INT NOT NULL,
  `sucursal_id` INT NOT NULL,
  `quantity` INT UNSIGNED NULL,
  INDEX `fk_products_has_sucursal_sucursal1_idx` (`sucursal_id` ASC) VISIBLE,
  INDEX `fk_products_has_sucursal_products1_idx` (`products_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_products_has_sucursal_products1`
    FOREIGN KEY (`products_id`)
    REFERENCES `grupal_project`.`products` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_products_has_sucursal_sucursal1`
    FOREIGN KEY (`sucursal_id`)
    REFERENCES `grupal_project`.`sucursal` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;