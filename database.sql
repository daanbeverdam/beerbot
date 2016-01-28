-- MySQL dump 10.13  Distrib 5.6.27, for osx10.8 (x86_64)
--
-- Host: localhost    Database: ke_beer
-- ------------------------------------------------------
-- Server version	5.6.27

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
-- Table structure for table `beer`
--

DROP TABLE IF EXISTS `beer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `beer` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `meal` varchar(255) NOT NULL,
  `mealcategory` varchar(255) NOT NULL DEFAULT '',
  `kind` varchar(255) NOT NULL DEFAULT '',
  `sweetness` varchar(255) NOT NULL DEFAULT '',
  `bitterness` int(11) NOT NULL,
  `color` varchar(255) NOT NULL DEFAULT '',
  `percentage` float(10,1) NOT NULL,
  `description` varchar(255) NOT NULL DEFAULT '',
  `imageid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beer`
--

LOCK TABLES `beer` WRITE;
/*!40000 ALTER TABLE `beer` DISABLE KEYS */;
INSERT INTO `beer` VALUES (1,'Guinness','oysters','fish','Stout','2',4,'dark',4.2,'',1),(2,'Guinness','stew','meat','Stout','2',4,'dark',4.2,'',1),(3,'Grolsch Herfstbok','nuts','nuts','Herfstbock','4',1,'dark',6.6,'',2),(4,'Grolsch Herfstbok','ripe cheese','cheese','Herfstbock','4',1,'dark',6.6,'',2),(5,'Grolsch Herfstbok','wild dish','meat','Herfstbock','4',1,'dark',6.6,'',2),(6,'Westmalle Dubbel','old cheese','cheese','Dubbel','3',3,'dark',7.0,'',3),(7,'Westmalle Dubbel','stew meat','meat','Dubbel','3',3,'dark',7.0,'',3),(8,'Grimbergen Dubbel','pancakes','sweets','Dubbel','4',4,'dark',6.5,'',4),(9,'Grimbergen Dubbel','bitterballen','meat','Dubbel','4',4,'dark',6.5,'',4),(10,'Kasteelbier Bruin','spicy sausage','meat','Dubbel','4',3,'dark',11.0,'',5),(11,'Kasteelbier Bruin','creme brulee','dessert','Dubbel','4',3,'dark',11.0,'',5),(12,'Straffe Hendrik Quadrupel','gorgonzola','cheese','Quadrupel','3',3,'dark',11.0,'',6),(13,'Straffe Hendrik Quadrupel','blue cheese','cheese','Quadrupel','3',3,'dark',11.0,'',6),(14,'Jopen Johannieter','smoked duck','poultry','Dubbelbok','4',4,'dark',9.0,'',7),(15,'Jopen Johannieter','wilde meat','meat','Dubbelbok','4',4,'dark',9.0,'',7),(16,'Kompaan','grill sausage','meat','Stout','4',4,'dark',7.1,'',8),(17,'Kompaan','barbecue','meat','Stout','4',4,'dark',7.1,'',8),(18,'Brooklyn Brewery Lager','bitterbal','meat','Amberbeer','2',2,'dark',5.2,'',9),(19,'Brooklyn Brewery Lager','hamburger','meat','Amberbeer','2',2,'dark',5.2,'',9),(20,'Heineken Oud Bruin','sausage','meat','Old Brown','4',2,'dark',2.5,'',10),(21,'Heineken Oud Bruin','spaghetti','meat','Old Brown','4',2,'dark',2.5,'',10),(22,'Hoegaarden Verboden vrucht','cheese','cheese','Overig Donker','4',2,'dark',8.5,'',11),(23,'Hoegaarden Verboden vrucht','liver sausage','meat','Overig Donker','4',2,'dark',8.5,'',11),(24,'Hoegaarden Verboden vrucht','oven dish','vegetarian','Overig Donker','4',2,'dark',8.5,'',11),(25,'De Leckere Blauwe bijl','dried fruit','vegetarian','Overig Donker','3',4,'dark',10.0,'',12),(26,'De Leckere Blauwe bijl','wild','meat','Overig Donker','3',4,'dark',10.0,'',12),(27,'La Chouffe Bier','tuna','fish','Blond','3',1,'light',8.5,'',13),(28,'La Chouffe Bier','red meat','meat','Blond','3',1,'light',8.5,'',13),(29,'Hoegaarden Grand Cru','calf meat','meat','Blond','3',3,'light',8.7,'',14),(30,'Hoegaarden Grand Cru','shrimp','fish','Blond','3',3,'light',8.7,'',14),(31,'Karmeliet Tripel','oysters','fish','Tripel','1',5,'light',8.5,'',15),(32,'Karmeliet Tripel','oven dish','vegetarian','Tripel','1',5,'light',8.5,'',15),(33,'Zundert Trappist','chicken','poultry','Tripel','2',4,'light',8.0,'',16),(34,'Zundert Trappist','asian','vegetarian','Tripel','2',4,'light',8.0,'',16),(35,'Chimay Tripel','oysters','fish','Tripel','3',1,'light',8.0,'',17),(36,'Chimay Tripel','tuna','fish','Tripel','3',1,'light',8.0,'',17),(37,'BrewDog Dead pony','englisch cheese','cheese','IPA','2',4,'light',3.8,'Volle citrusaroma\'s van pittige limoen en citroengras exploderen uit het glas, tegenover een lichte caramelgeur met een bloeiende harsachtige hop aroma als afsluiter',18),(38,'BrewDog Dead pony','hamburger','meat','IPA','2',4,'light',3.8,'Volle citrusaroma\'s van pittige limoen en citroengras exploderen uit het glas, tegenover een lichte caramelgeur met een bloeiende harsachtige hop aroma als afsluiter',18),(39,'Goose Island IPA','blue cheese','cheese','IPA','2',5,'light',5.9,'',19),(40,'Goose Island IPA','curry','fish','IPA','2',5,'light',5.9,'',19),(41,'Brand IPA','smoked salmon','fish','IPA','4',3,'light',7.0,'Brand IPA is gebrouwen met drie hopsoorten (Cascade-, Citra- en Amarillo-hop). Kenmerkt zich door fruitig citrusachtige smaak met zacht bittere afdronk.',20),(42,'Brand IPA','satay','poultry','IPA','4',3,'light',7.0,'Brand IPA is gebrouwen met drie hopsoorten (Cascade-, Citra- en Amarillo-hop). Kenmerkt zich door fruitig citrusachtige smaak met zacht bittere afdronk.',20),(43,'Grolsch Kanon','dried fruit','vegetarian','Gerstewijn','2',4,'light',11.6,'Grolsch Krachtig Kanon is een volgouden bier, krachtig en machtig van smaak. Eerst valt de zoetheid op die langzaam wordt overgenomen door een aangename prikkeling op de tong.',21),(44,'Grolsch Kanon','ham','meat','Gerstewijn','2',4,'light',11.6,'Grolsch Krachtig Kanon is een volgouden bier, krachtig en machtig van smaak. Eerst valt de zoetheid op die langzaam wordt overgenomen door een aangename prikkeling op de tong.',21),(45,'Gulden Draak','spicy sausage','meat','Gerstewijn','1',4,'light',10.5,'',22),(46,'Gulden Draak','red meat','meat','Gerstewijn','1',4,'light',10.5,'',22),(47,'De Prael Bitterblond','mild cheese','cheese','Blond','3',4,'light',5.7,'',23),(48,'De Prael Bitterblond','bitterbal','meat','Blond','3',4,'light',5.7,'',23),(49,'De Prael IPA','sushi','fish','IPA','3',4,'light',7.5,'',24),(50,'De Prael IPA','curry','vegetarian','IPA','3',4,'light',7.5,'',24),(51,'Oedipus Mama','spicy chicken','poultry','IPA','3',3,'light',5.0,'',25),(52,'Oedipus Mama','curry','vegetarian','IPA','3',3,'light',5.0,'',25),(53,'Vedett Extra white','spring roll','meat','Witbier','4',3,'light',4.7,'',26),(54,'Vedett Extra white','mussels','fish','Witbier','4',3,'light',4.7,'',26),(55,'Jopen Adriaan','sushi','fish','Witbier','3',2,'light',5.0,'',27),(56,'Jopen Adriaan','fish dish','fish','Witbier','3',2,'light',5.0,'',27),(57,'Texels Skuumkoppe','cheese','cheese','Witbier','3',3,'light',6.0,'',28),(58,'Texels Skuumkoppe','white fish','fish','Witbier','3',3,'light',6.0,'',28),(59,'Weihenstephaner Hefe Weissbier','sushi','fish','Witbier','4',2,'light',5.0,'De herkenbare smaak van geel fruit zoals banaan hebben deze bieren enkel te danken aan de speciale gist die wordt gebruikt. Er worden, zoals het Reihnheitsgebot voorschrijft geen extra smaakmakers toegevoegd aan het bier.',29),(60,'Weihenstephaner Hefe weissbier','fish pasta','fish','Witbier','4',2,'light',5.0,'De herkenbare smaak van geel fruit zoals banaan hebben deze bieren enkel te danken aan de speciale gist die wordt gebruikt. Er worden, zoals het Reihnheitsgebot voorschrijft geen extra smaakmakers toegevoegd aan het bier.',29),(61,'Wieckse Rosé','tapas','vegetarian','Rosébier','5',2,'light',4.0,'Wieckse Rosé heeft de nuance van een rosé en het verfrissende van witbier. De combinatie met vruchtensappen geven Wieckse Rosé witbier haar friszoete smaak en mooie rosé kleur.',30),(62,'Wieckse Rosé','salad','vegetarian','Rosébier','5',2,'light',4.0,'Wieckse Rosé heeft de nuance van een rosé en het verfrissende van witbier. De combinatie met vruchtensappen geven Wieckse Rosé witbier haar friszoete smaak en mooie rosé kleur.',30),(63,'Stella Artois Cidre','salted meat','meat','Cider','5',1,'light',4.5,'',31),(64,'Stella Artois Cidre','pork loin','meat','Cider','5',1,'light',4.5,'',31),(65,'Somersby Blackberry Cider','tapas','meat','Cider','5',2,'light',4.5,'Cider with a taste of Blackberry.',32),(66,'Somersby Blackberry Cider','turkey','poultry','Cider','5',2,'light',4.5,'Cider with a taste of Blackberry.',32),(67,'Somersby Blackberry Cider','chicken','poultry','Cider','5',2,'light',4.5,'Cider with a taste of Blackberry.',32),(68,'Lindemans Framboise','chocolate','sweets','Fruitbier','5',2,'light',2.5,'',33),(69,'Lindemans Framboise','cabbage','vegetarian','Fruitbier','5',2,'light',2.5,'',33),(70,'Liefmans Fruitesse ','fruit','vegetarian','Fruitbier','5',1,'light',3.8,'',34),(71,'Liefmans Fruitesse ','chocolate','sweets','Fruitbier','5',1,'light',3.8,'',34),(72,'Sol Mexican Beer','nacho','vegetarian','Mexicaans','3',1,'light',4.5,'',35),(73,'Sol Mexican Beer','wraps','meat','Mexicaans','3',1,'light',4.5,'',35),(74,'Dupont Saison','white fish','fish','Saison','3',3,'light',6.5,'',36),(75,'Dupont Saison','soft cheese','cheese','Saison','3',3,'light',6.5,'',36);
/*!40000 ALTER TABLE `beer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mealcategory`
--

DROP TABLE IF EXISTS `mealcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mealcategory` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mealcategory`
--

LOCK TABLES `mealcategory` WRITE;
/*!40000 ALTER TABLE `mealcategory` DISABLE KEYS */;
INSERT INTO `mealcategory` VALUES (1,'fish'),(2,'meat'),(3,'nuts'),(4,'cheese'),(5,'dessert'),(6,'poultry'),(7,'vegetarian'),(8,'sweets');
/*!40000 ALTER TABLE `mealcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `chat_id` int(11) unsigned NOT NULL,
  `name` varchar(255) NOT NULL DEFAULT '',
  `color` varchar(255) DEFAULT NULL,
  `bitterness` int(11) DEFAULT NULL,
  `sweetness` int(11) DEFAULT NULL,
  `percentage` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-28 16:35:51
