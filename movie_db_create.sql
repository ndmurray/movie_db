-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema movie_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema movie_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `movie_db` DEFAULT CHARACTER SET utf8 ;
USE `movie_db` ;

-- -----------------------------------------------------
-- Table `movie_db`.`title`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`title` (
  `title_id` VARCHAR(10) NOT NULL,
  `titleType` VARCHAR(100) NULL,
  `primaryTitle` VARCHAR(500) NOT NULL,
  `originalTitle` VARCHAR(500) NULL,
  `isAdult` TINYINT(1) NULL,
  `startYear` VARCHAR(4) NULL,
  `endYear` VARCHAR(4) NULL,
  `runtimeMinutes` VARCHAR(10) NULL,
  `genres` VARCHAR(255) NULL,
  `averageRating` FLOAT NULL,
  `numVotes` INT NULL,
  PRIMARY KEY (`title_id`),
  UNIQUE INDEX `title_id_UNIQUE` (`title_id` ASC) VISIBLE)
ENGINE = InnoDB;


LOAD DATA LOCAL INFILE './app_data/title.csv'
INTO TABLE title
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';

-- -----------------------------------------------------
-- Table `movie_db`.`actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`actor` (
  `actor_id` VARCHAR(10) NOT NULL,
  `primaryName` VARCHAR(255) NOT NULL,
  `birthYear` VARCHAR(4) NULL,
  `deathYear` VARCHAR(4) NULL,
  `knownForTitles` VARCHAR(255) NULL,
  PRIMARY KEY (`actor_id`),
  UNIQUE INDEX `actor_id_UNIQUE` (`actor_id` ASC) VISIBLE)
ENGINE = InnoDB;

LOAD DATA LOCAL INFILE './app_data/actor.csv'
INTO TABLE actor
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';


-- -----------------------------------------------------
-- Table `movie_db`.`actor_lookup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`actor_lookup` (
  `actor_lookup_id` INT NOT NULL AUTO_INCREMENT,
  `actor_id` VARCHAR(10) NOT NULL,
  `a_title_id` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`actor_lookup_id`),
  UNIQUE INDEX `actors_lookup_id_UNIQUE` (`actor_lookup_id` ASC) VISIBLE,
  INDEX `title_id_idx` (`a_title_id` ASC) VISIBLE,
  INDEX `actor_id_idx` (`actor_id` ASC) VISIBLE,
  CONSTRAINT `a_title_id`
    FOREIGN KEY (`a_title_id`)
    REFERENCES `movie_db`.`title` (`title_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `actor_id`
    FOREIGN KEY (`actor_id`)
    REFERENCES `movie_db`.`actor` (`actor_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


LOAD DATA LOCAL INFILE './app_data/actor_lookup.csv'
INTO TABLE actor_lookup
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';

-- -----------------------------------------------------
-- Table `movie_db`.`director`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`director` (
  `director_id` VARCHAR(10) NOT NULL,
  `primaryName` VARCHAR(255) NOT NULL,
  `birthYear` VARCHAR(4) NULL,
  `deathYear` VARCHAR(4) NULL,
  `knownForTitles` VARCHAR(255) NULL,
  PRIMARY KEY (`director_id`),
  UNIQUE INDEX `director_id_UNIQUE` (`director_id` ASC) VISIBLE)
ENGINE = InnoDB;

LOAD DATA LOCAL INFILE './app_data/director.csv'
INTO TABLE director
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';


-- -----------------------------------------------------
-- Table `movie_db`.`director_lookup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`director_lookup` (
  `director_lookup_id` INT NOT NULL AUTO_INCREMENT,
  `d_title_id` VARCHAR(10) NOT NULL,
  `director_id` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`director_lookup_id`),
  UNIQUE INDEX `director_lookup_id_UNIQUE` (`director_lookup_id` ASC) VISIBLE,
  INDEX `director_id_idx` (`director_id` ASC) VISIBLE,
  INDEX `d_title_id_idx` (`d_title_id` ASC) VISIBLE,
  CONSTRAINT `d_title_id`
    FOREIGN KEY (`d_title_id`)
    REFERENCES `movie_db`.`title` (`title_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `director_id`
    FOREIGN KEY (`director_id`)
    REFERENCES `movie_db`.`director` (`director_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

LOAD DATA LOCAL INFILE './app_data/director_lookup.csv'
INTO TABLE director_lookup
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';


-- -----------------------------------------------------
-- Table `movie_db`.`writer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`writer` (
  `writer_id` VARCHAR(10) NOT NULL,
  `primaryName` VARCHAR(255) NOT NULL,
  `birthYear` VARCHAR(4) NULL,
  `deathYear` VARCHAR(4) NULL,
  `knownForTitles` VARCHAR(255) NULL,
  PRIMARY KEY (`writer_id`),
  UNIQUE INDEX `writer_id_UNIQUE` (`writer_id` ASC) VISIBLE)
ENGINE = InnoDB;

LOAD DATA LOCAL INFILE './app_data/writer.csv'
INTO TABLE writer
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';


-- -----------------------------------------------------
-- Table `movie_db`.`writer_lookup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_db`.`writer_lookup` (
  `writer_lookup_id` INT NOT NULL AUTO_INCREMENT,
  `w_title_id` VARCHAR(10) NOT NULL,
  `writer_id` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`writer_lookup_id`),
  UNIQUE INDEX `writer_lookup_id_UNIQUE` (`writer_lookup_id` ASC) VISIBLE,
  INDEX `title_id_idx` (`w_title_id` ASC) VISIBLE,
  INDEX `writer_id_idx` (`writer_id` ASC) VISIBLE,
  CONSTRAINT `w_title_id`
    FOREIGN KEY (`w_title_id`)
    REFERENCES `movie_db`.`title` (`title_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `writer_id`
    FOREIGN KEY (`writer_id`)
    REFERENCES `movie_db`.`writer` (`writer_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

LOAD DATA LOCAL INFILE './app_data/writer_lookup.csv'
INTO TABLE writer_lookup
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n';



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
