-- Author:Ondrej Kulhavy
-- Email: okulhav@gmail.com
-- Date: 2024-02-04
-- Project: E-prescription

START TRANSACTION;
CREATE DATABASE  IF NOT EXISTS `e_prescription` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `e_prescription`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: e_prescription
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `TITLE` varchar(100) NOT NULL,
  `FIRST_NAME` varchar(100) NOT NULL,
  `MIDDLE_NAME` varchar(100) DEFAULT NULL,
  `LAST_NAME` varchar(100) NOT NULL,
  `PHONE` varchar(16) NOT NULL,
  `EMAIL` varchar(100) NOT NULL,
  `SPECIALIZATION_ID` int NOT NULL,
  `date_of_birth` date NOT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `SPECIALIZATION_ID` (`SPECIALIZATION_ID`),
  CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`SPECIALIZATION_ID`) REFERENCES `specialization` (`ID`),
  CONSTRAINT `doctor_chk_1` CHECK (regexp_like(`PHONE`,_utf8mb4'^[+]?[(]?[0-9]{3}[)]?[-s.]?[0-9]{3}[-s.]?[0-9]{4,6}$')),
  CONSTRAINT `doctor_chk_2` CHECK (regexp_like(`EMAIL`,_utf8mb4'[^@ 	\r\n]+@[^@ 	\r\n]+.[^@ 	\r\n]+'))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'MUDr.','Admin',NULL,'Admin','+420123456789','admin@email.cz',1,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(2,'MUDr.','Eva',NULL,'Svobodová','+420987654321','esvobodova@email.cz',2,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(3,'MUDr.','Petr',NULL,'Václavík','+420456789123','pvaclavik@email.cz',3,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(4,'MUDr.','Anna',NULL,'Dvořáková','+420789123456','advorakova@email.cz',4,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(5,'MUDr.','Lukáš',NULL,'Horák','+420321654987','lhorak@email.cz',5,'1982-04-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(6,'MUDr.','Kateřina',NULL,'Jirásková','+420654321789','kjiraskova@email.cz',6,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(7,'MUDr.','Martin',NULL,'Zeman','+420432567891','mzeman@email.cz',7,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(8,'MUDr.','Lenka',NULL,'Křížová','+420765432198','lkrižova@email.cz',8,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(9,'MUDr.','Tomáš',NULL,'Hrubý','+420198765432','thruby@email.cz',9,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU'),(10,'MUDr.','Jana',NULL,'Šťastná','+420234567890','jstastna@email.cz',10,'1982-02-10','$pbkdf2-sha256$29000$/j.ndA5hLAVACOE8h7C21g$bH0e833m6k.iALH9nO8X/M96p2FL0TZkULtk4LLufTU');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `doctorspecializationview`
--

DROP TABLE IF EXISTS `doctorspecializationview`;
/*!50001 DROP VIEW IF EXISTS `doctorspecializationview`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `doctorspecializationview` AS SELECT 
 1 AS `DoctorID`,
 1 AS `DoctorTitle`,
 1 AS `DoctorFirstName`,
 1 AS `DoctorLastName`,
 1 AS `DoctorPhone`,
 1 AS `DoctorEmail`,
 1 AS `SpecializationName`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `drug`
--

DROP TABLE IF EXISTS `drug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) NOT NULL,
  `PRICE` float NOT NULL,
  `ACTIVE_SUBSTANCE` varchar(255) NOT NULL,
  `FORM` int NOT NULL,
  `DESCRIPTION` varchar(2000) NOT NULL,
  `SIDE_EFFECTS` varchar(2000) NOT NULL,
  `STORAGE_CONDITIONS` varchar(2000) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FORM` (`FORM`),
  CONSTRAINT `drug_ibfk_1` FOREIGN KEY (`FORM`) REFERENCES `drug_form` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug`
--

LOCK TABLES `drug` WRITE;
/*!40000 ALTER TABLE `drug` DISABLE KEYS */;
INSERT INTO `drug` VALUES (1,'Paralen',49.9,'paracetamol',1,'Paralen je léčivý přípravek, který se používá k úlevě od bolesti a snížení horečky. Paralen je vhodný pro dospělé i děti od 6 let.','Paralen může způsobovat nežádoucí účinky, jako jsou alergické reakce, poruchy krve, poškození jater nebo ledvin, pokud se užívá v nadměrných dávkách nebo po dlouhou dobu.','Paralen se uchovává při teplotě do 25 °C, mimo dosah dětí a před světlem chráněný.'),(2,'Ibuprofen',59.9,'ibuprofen',1,'Ibuprofen je léčivý přípravek, který se používá k úlevě od bolesti, zánětu a horečky. Ibuprofen je vhodný pro dospělé i děti od 12 let.','Ibuprofen může způsobovat nežádoucí účinky, jako jsou zažívací potíže, vředy, krvácení, alergické reakce, poruchy srdečního rytmu, zvýšený krevní tlak, poškození jater nebo ledvin, pokud se užívá v nadměrných dávkách nebo po dlouhou dobu.','Ibuprofen se uchovává při teplotě do 25 °C, mimo dosah dětí a před vlhkostí chráněný.'),(3,'Nurofen',79.9,'ibuprofen',2,'Nurofen je léčivý přípravek, který se používá k úlevě od bolesti, zánětu a horečky. Nurofen je vhodný pro dospělé i děti od 12 let.','Nurofen může způsobovat nežádoucí účinky, jako jsou zažívací potíže, vředy, krvácení, alergické reakce, poruchy srdečního rytmu, zvýšený krevní tlak, poškození jater nebo ledvin, pokud se užívá v nadměrných dávkách nebo po dlouhou dobu.','Nurofen se uchovává při teplotě do 25 °C, mimo dosah dětí a před vlhkostí chráněný.'),(4,'Aspirin',69.9,'kyselina acetylsalicylová',1,'Aspirin je léčivý přípravek, který se používá k úlevě od bolesti, zánětu, horečky a prevenci srdečních a cévních onemocnění. Aspirin je vhodný pro dospělé, ale nesmí se podávat dětem a dospívajícím s horečkou.','Aspirin může způsobovat nežádoucí účinky, jako jsou zažívací potíže, vředy, krvácení, alergické reakce, poruchy srážení krve, zhoršení astmatu, poškození jater nebo ledvin, pokud se užívá v nadměrných dávkách nebo po dlouhou dobu.','Aspirin se uchovává při teplotě do 25 °C, mimo dosah dětí a před světlem chráněný.'),(5,'Zinnat',199.9,'cefuroxim',3,'Zinnat je antibiotikum, které se používá k léčbě různých bakteriálních infekcí, jako jsou angína, zánět středního ucha, zánět močových cest, zánět plic, borelióza a další. Zinnat je vhodný pro dospělé i děti od 3 měsíců.','Zinnat může způsobovat nežádoucí účinky, jako jsou alergické reakce, zažívací potíže, průjem, kandidóza, poruchy krve, zvýšené hladiny jaterních enzymů, pokud se užívá v nadměrných dávkách nebo po dlouhou dobu.','Zinnat se uchovává při teplotě do 25 °C, mimo dosah dětí a před vlhkostí chráněný.'),(6,'Test',100.1,'Test',3,'Test','Test','Test');
/*!40000 ALTER TABLE `drug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drug_form`
--

DROP TABLE IF EXISTS `drug_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug_form` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug_form`
--

LOCK TABLES `drug_form` WRITE;
/*!40000 ALTER TABLE `drug_form` DISABLE KEYS */;
INSERT INTO `drug_form` VALUES (1,'tableta'),(2,'tobolka'),(3,'sirup'),(4,'injekce'),(5,'čípek'),(6,'krém'),(7,'gel'),(8,'kapka'),(9,'náplast'),(10,'mýdlo');
/*!40000 ALTER TABLE `drug_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `drugregisterview`
--

DROP TABLE IF EXISTS `drugregisterview`;
/*!50001 DROP VIEW IF EXISTS `drugregisterview`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `drugregisterview` AS SELECT 
 1 AS `DrugID`,
 1 AS `DrugName`,
 1 AS `DrugPrice`,
 1 AS `ActiveSubstance`,
 1 AS `DrugForm`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `insurance_company`
--

DROP TABLE IF EXISTS `insurance_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insurance_company` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `CODE` int NOT NULL,
  `ABBREVIATION` varchar(4) NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `STREET` varchar(100) NOT NULL,
  `HOUSE` int NOT NULL,
  `CITY` varchar(150) NOT NULL,
  `PSC` int NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `insurance_company_chk_1` CHECK (regexp_like(`ABBREVIATION`,_utf8mb4'^[A-Z]+$'))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insurance_company`
--

LOCK TABLES `insurance_company` WRITE;
/*!40000 ALTER TABLE `insurance_company` DISABLE KEYS */;
INSERT INTO `insurance_company` VALUES (1,205,'CPZP','Česká průmyslová zdravotní pojišťovna','Na Poříčí',25,'Praha 1',11000),(2,207,'OZP','Oborová zdravotní pojišťovna zaměstnanců bank, pojišťoven a stavebnictví','Na Příkopě',33,'Praha 1',11000),(3,213,'RBP','RBP, zdravotní pojišťovna','Václavské náměstí',56,'Praha 1',11000),(4,111,'VZP','Všeobecná zdravotní pojišťovna České republiky','Orlická',4,'Praha 10',10034),(5,201,'VOZP','Vojenská zdravotní pojišťovna ČR','Evropská',17,'Praha 6',16000),(6,209,'ZPS','Zaměstnanecká pojišťovna Škoda','Tylova',57,'Plzeň',30100),(7,211,'ZPMV','Zdravotní pojišťovna ministerstva vnitra','Budějovická',20,'Praha 4',14000);
/*!40000 ALTER TABLE `insurance_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `PHONE` varchar(16) NOT NULL,
  `EMAIL` varchar(100) NOT NULL,
  `STREET` varchar(100) NOT NULL,
  `HOUSE` int NOT NULL,
  `CITY` varchar(150) NOT NULL,
  `PSC` int NOT NULL,
  `INSURANCE_COMPANY_ID` int NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_INSURANCE_COMPANY` (`INSURANCE_COMPANY_ID`),
  CONSTRAINT `FK_INSURANCE_COMPANY` FOREIGN KEY (`INSURANCE_COMPANY_ID`) REFERENCES `insurance_company` (`ID`),
  CONSTRAINT `patient_chk_1` CHECK (regexp_like(`PHONE`,_utf8mb4'^[+]?[(]?[0-9]{3}[)]?[-s.]?[0-9]{3}[-s.]?[0-9]{4,6}$')),
  CONSTRAINT `patient_chk_2` CHECK (regexp_like(`EMAIL`,_utf8mb4'[^@ 	\r\n]+@[^@ 	\r\n]+.[^@ 	\r\n]+'))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'+420123456789','jan.novak@email.cz','Náměstí Míru',12,'Praha',12000,1,'1980-02-06','Jan',NULL,'Novak'),(2,'+420987654321','eva.dvorakova@email.cz','Husova',8,'Brno',60200,2,'1980-02-06','Eva',NULL,'Dvorakova'),(3,'+420456789123','petr.svoboda@email.cz','Masarykova',15,'Plzeň',30100,1,'1980-02-06','Petr',NULL,'Svoboda'),(4,'+420789123456','anna.horakova@email.cz','Komenského',10,'Olomouc',77900,2,'1980-02-06','Anna','Tereza','Horakova'),(5,'+420321654987','lukas.vaclavik@email.cz','Palackého',5,'Ostrava',70200,3,'1980-02-06','Lukas',NULL,'Vaclavik'),(6,'+420654321789','katerina.jiraskova@email.cz','Tyršova',7,'Liberec',46001,4,'1980-02-06','Katerina',NULL,'Jiraskova'),(7,'+420147258369','martin.zeman@email.cz','Karlova',9,'České Budějovice',37001,1,'1980-02-06','Martin',NULL,'Zeman'),(8,'+420369258147','jana.novotna@email.cz','Jiráskova',6,'Hradec Králové',50002,1,'1980-02-06','Jana',NULL,'Novotna'),(9,'+420258369147','tomas.prochazka@email.cz','Nerudova',4,'Pardubice',53002,1,'1980-02-06','Tomas',NULL,'Prochazka'),(10,'+420963852741','lenka.krizova@email.cz','Kollárova',3,'Zlín',76001,1,'1980-02-06','Lenka',NULL,'Krizova'),(11,'+420123123123','kahoun@spsejecna.cz','Jecna',30,'Praha 2',11111,4,'2005-12-12','Daniel','','Kahoun');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prescription`
--

DROP TABLE IF EXISTS `prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescription` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `PATIENT_ID` int NOT NULL,
  `ISSUED_BY_DOCTOR_ID` int NOT NULL,
  `ISSUED_DATE` date NOT NULL,
  `VALID_UNTIL` date NOT NULL,
  `STATUS` enum('vydaný','zrušený','použitý') NOT NULL DEFAULT 'vydaný',
  `TYPE` enum('běžné','pohotovostní','náhradní','dlouhodobé') NOT NULL DEFAULT 'běžné',
  PRIMARY KEY (`ID`),
  KEY `PATIENT_ID` (`PATIENT_ID`),
  KEY `ISSUED_BY_DOCTOR_ID` (`ISSUED_BY_DOCTOR_ID`),
  CONSTRAINT `prescription_ibfk_1` FOREIGN KEY (`PATIENT_ID`) REFERENCES `patient` (`ID`),
  CONSTRAINT `prescription_ibfk_2` FOREIGN KEY (`ISSUED_BY_DOCTOR_ID`) REFERENCES `doctor` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescription`
--

LOCK TABLES `prescription` WRITE;
/*!40000 ALTER TABLE `prescription` DISABLE KEYS */;
INSERT INTO `prescription` VALUES (1,1,1,'2024-01-31','2024-02-28','vydaný','běžné'),(2,2,2,'2024-01-31','2024-02-28','vydaný','pohotovostní'),(3,3,3,'2024-01-31','2024-02-28','vydaný','náhradní'),(4,4,4,'2024-01-31','2024-02-28','vydaný','dlouhodobé'),(5,5,5,'2024-01-31','2024-02-28','vydaný','běžné'),(6,6,1,'2024-01-31','2024-03-01','vydaný','běžné'),(7,7,2,'2024-01-31','2024-03-01','vydaný','pohotovostní'),(8,8,3,'2024-01-31','2024-03-01','vydaný','náhradní'),(9,9,4,'2024-01-31','2024-03-01','vydaný','dlouhodobé'),(10,10,5,'2024-01-31','2024-03-01','vydaný','běžné'),(11,1,1,'2024-02-04','2030-12-12','vydaný','běžné'),(12,1,1,'2024-02-04','2030-12-12','vydaný','běžné');
/*!40000 ALTER TABLE `prescription` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `PRESCRIPTION_BEFORE_INSERT` BEFORE INSERT ON `prescription` FOR EACH ROW BEGIN

    IF NEW.VALID_UNTIL < NEW.ISSUED_DATE THEN

        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The prescription cannot be valid until before it is issued';

    END IF;



    SET NEW.ISSUED_DATE = CURDATE();

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `prescription_item`
--

DROP TABLE IF EXISTS `prescription_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prescription_item` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `PRESCRIPTION_ID` int NOT NULL,
  `DRUG_ID` int NOT NULL,
  `QUANTITY` int NOT NULL,
  `DOSAGE` varchar(255) NOT NULL,
  `INSTRUCTIONS` varchar(500) NOT NULL,
  `PICKED_UP` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `PRESCRIPTION_ID` (`PRESCRIPTION_ID`),
  KEY `DRUG_ID` (`DRUG_ID`),
  CONSTRAINT `prescription_item_ibfk_1` FOREIGN KEY (`PRESCRIPTION_ID`) REFERENCES `prescription` (`ID`),
  CONSTRAINT `prescription_item_ibfk_2` FOREIGN KEY (`DRUG_ID`) REFERENCES `drug` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prescription_item`
--

LOCK TABLES `prescription_item` WRITE;
/*!40000 ALTER TABLE `prescription_item` DISABLE KEYS */;
INSERT INTO `prescription_item` VALUES (1,1,1,2,'Jednou denně','S vodou',0),(2,2,2,1,'Dvakrát denně','S jídlem',1),(3,3,3,3,'Podle potřeby','Žádná specifická instrukce',0),(4,4,4,1,'Jednou před spaním','Vyhnout se alkoholu',1),(5,5,5,2,'Každých 6 hodin','Nerozdrvičkovat',0),(6,6,1,2,'Jednou denně','S vodou',0),(7,7,2,1,'Dvakrát denně','S jídlem',1),(8,8,3,3,'Podle potřeby','Žádná specifická instrukce',0),(9,9,4,1,'Jednou před spaním','Vyhnout se alkoholu',1),(10,10,5,2,'Každých 6 hodin','Nerozdrvičkovat',0),(11,12,1,3,'Test','Test',0);
/*!40000 ALTER TABLE `prescription_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `prescriptionwithpatientview`
--

DROP TABLE IF EXISTS `prescriptionwithpatientview`;
/*!50001 DROP VIEW IF EXISTS `prescriptionwithpatientview`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `prescriptionwithpatientview` AS SELECT 
 1 AS `PrescriptionID`,
 1 AS `DoctorID`,
 1 AS `IssuedDate`,
 1 AS `ValidUntil`,
 1 AS `Status`,
 1 AS `Type`,
 1 AS `PatientID`,
 1 AS `PatientFirstName`,
 1 AS `PatientLastName`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `specialization`
--

DROP TABLE IF EXISTS `specialization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialization` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialization`
--

LOCK TABLES `specialization` WRITE;
/*!40000 ALTER TABLE `specialization` DISABLE KEYS */;
INSERT INTO `specialization` VALUES (1,'psychiatrie'),(2,'dermatovenerologie'),(3,'kardiologie'),(4,'endokrinologie'),(5,'revmatologie'),(6,'neurologie'),(7,'onkologie'),(8,'pediatrie'),(9,'gynekologie'),(10,'urologie');
/*!40000 ALTER TABLE `specialization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'e_prescription'
--

--
-- Dumping routines for database 'e_prescription'
--

--
-- Final view structure for view `doctorspecializationview`
--

/*!50001 DROP VIEW IF EXISTS `doctorspecializationview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `doctorspecializationview` AS select `d`.`ID` AS `DoctorID`,`d`.`TITLE` AS `DoctorTitle`,`d`.`FIRST_NAME` AS `DoctorFirstName`,`d`.`LAST_NAME` AS `DoctorLastName`,`d`.`PHONE` AS `DoctorPhone`,`d`.`EMAIL` AS `DoctorEmail`,`s`.`NAME` AS `SpecializationName` from (`doctor` `d` join `specialization` `s` on((`d`.`SPECIALIZATION_ID` = `s`.`ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `drugregisterview`
--

/*!50001 DROP VIEW IF EXISTS `drugregisterview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `drugregisterview` AS select `d`.`ID` AS `DrugID`,`d`.`NAME` AS `DrugName`,`d`.`PRICE` AS `DrugPrice`,`d`.`ACTIVE_SUBSTANCE` AS `ActiveSubstance`,`df`.`NAME` AS `DrugForm` from (`drug` `d` join `drug_form` `df` on((`d`.`FORM` = `df`.`ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `prescriptionwithpatientview`
--

/*!50001 DROP VIEW IF EXISTS `prescriptionwithpatientview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `prescriptionwithpatientview` AS select `p`.`ID` AS `PrescriptionID`,`p`.`ISSUED_BY_DOCTOR_ID` AS `DoctorID`,`p`.`ISSUED_DATE` AS `IssuedDate`,`p`.`VALID_UNTIL` AS `ValidUntil`,`p`.`STATUS` AS `Status`,`p`.`TYPE` AS `Type`,`pa`.`ID` AS `PatientID`,`pa`.`first_name` AS `PatientFirstName`,`pa`.`last_name` AS `PatientLastName` from (`prescription` `p` join `patient` `pa` on((`p`.`PATIENT_ID` = `pa`.`ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-04 22:08:10

COMMIT;