-- -------------------------------------------------------------
-- TablePlus 5.1.0(468)
--
-- https://tableplus.com/
--
-- Database: students
-- Generation Time: 2022-11-20 18:02:14.3670
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP TABLE IF EXISTS `program`;
CREATE TABLE `program` (
  `pr_id` varchar(255) NOT NULL,
  `pr_name` varchar(255) NOT NULL,
  PRIMARY KEY (`pr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `index_no` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `program` varchar(255) NOT NULL,
  `level` int NOT NULL,
  `cgpa` decimal(10,0) NOT NULL,
  PRIMARY KEY (`index_no`),
  KEY `program` (`program`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`program`) REFERENCES `program` (`pr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `staff_id` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` int NOT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `program` (`pr_id`, `pr_name`) VALUES
('BT_CS', 'BTECH Computer Science'),
('BT_ICT', 'BTECH ICT'),
('HND_CS', 'HND Computer Science'),
('HND_IT', 'HND ICT');

INSERT INTO `students` (`index_no`, `first_name`, `last_name`, `program`, `level`, `cgpa`) VALUES
('001', 'Emmanuel', 'Sewor', 'BT_ICT', 400, 5),
('002', 'Emmanuel', 'John', 'BT_CS', 200, 4),
('003', 'Rina', 'Tsey', 'BT_ICT', 200, 4),
('004', 'Ophelia', 'Sewor', 'BT_CS', 100, 4),
('0320010012', 'Joe', 'Kwame', 'HND_IT', 300, 3),
('0320080013', 'Kwame', 'Sedem', 'HND_IT', 300, 4);

INSERT INTO `users` (`staff_id`, `password`, `role`) VALUES
('ST_001', '12345', 1);



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;