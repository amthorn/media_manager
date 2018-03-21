-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: media
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(1024) NOT NULL,
  `Year` int(11) DEFAULT NULL,
  `Rated` varchar(8) DEFAULT NULL,
  `Released` date DEFAULT NULL,
  `Runtime` varchar(64) DEFAULT NULL,
  `Genre` varchar(1024) DEFAULT NULL,
  `Director` varchar(1024) DEFAULT NULL,
  `Writer` varchar(1024) DEFAULT NULL,
  `Actors` varchar(1024) DEFAULT NULL,
  `Plot` varchar(2048) DEFAULT NULL,
  `Language` varchar(64) DEFAULT NULL,
  `Country` varchar(64) DEFAULT NULL,
  `Awards` varchar(1024) DEFAULT NULL,
  `Poster` varchar(2048) DEFAULT NULL,
  `Metascore` int(11) DEFAULT NULL,
  `imdbRating` float DEFAULT NULL,
  `imdbVotes` int(11) DEFAULT NULL,
  `imdbID` varchar(32) DEFAULT NULL,
  `Type` varchar(64) DEFAULT NULL,
  `DVD` date DEFAULT NULL,
  `BoxOffice` float DEFAULT NULL,
  `Production` varchar(2048) DEFAULT NULL,
  `Website` varchar(512) DEFAULT NULL,
  `Response` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Up',2009,'PG','2009-05-29','96 min','Animation, Adventure, Comedy','Pete Docter, Bob Peterson(co-director)','Pete Docter (story by), Bob Peterson (story by), Tom McCarthy (story by), Bob Peterson (screenplay by), Pete Docter (screenplay by)','Edward Asner, Christopher Plummer, Jordan Nagai, Bob Peterson','Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, inadvertently taking a young stowaway.','English','USA','Won 2 Oscars. Another 74 wins & 81 nominations.','https://ia.media-imdb.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_SX300.jpg',88,8.3,771869,'tt1049413','movie','2009-11-10',292980000,'Walt Disney Pictures','http://Disney.com/UP','True'),(2,'Saw',2004,'R','2004-10-29','103 min','Crime, Horror, Mystery','James Wan','Leigh Whannell, James Wan (story), Leigh Whannell (story)','Leigh Whannell, Cary Elwes, Danny Glover, Ken Leung','Two strangers, who awaken in a room with no recollection of how they got there, soon discover they\'re pawns in a deadly game perpetrated by a notorious serial killer.','English','USA','8 wins & 10 nominations.','https://images-na.ssl-images-amazon.com/images/M/MV5BMzQ2ZTBhNmEtZDBmYi00ODU0LTgzZmQtNmMxM2M4NzM1ZjE4XkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_SX300.jpg',46,7.7,332207,'tt0387564','movie','2005-02-15',55100000,'Lions Gate Films','http://www.sawmovie.com/','True');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-17  0:17:59
