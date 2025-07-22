/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - stressdetection_mes_kallanthode
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`stressdetection_mes_kallanthode` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `stressdetection_mes_kallanthode`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `Chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `Form_id` int(11) DEFAULT NULL,
  `To_id` int(11) DEFAULT NULL,
  `Chat` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `C_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_loginid` int(11) DEFAULT NULL,
  `Complaint` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Reply` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`C_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`C_id`,`User_loginid`,`Complaint`,`Date`,`Reply`,`Status`) values 
(1,2,'vhjghgvjhv','2022-10-06','rfhgdgf','replied'),
(2,0,'\"+complaint+\"','2022-12-10','pending','pending'),
(3,0,'\"+complaint+\"','2022-12-10','pending','pending');

/*Table structure for table `diary` */

DROP TABLE IF EXISTS `diary`;

CREATE TABLE `diary` (
  `D_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_loginid` int(11) DEFAULT NULL,
  `Diary` tinytext,
  `Date` date DEFAULT NULL,
  `Time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`D_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `diary` */

/*Table structure for table `emotion` */

DROP TABLE IF EXISTS `emotion`;

CREATE TABLE `emotion` (
  `Em_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_loginid` int(11) DEFAULT NULL,
  `Emotion` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Em_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `emotion` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'user','0','user'),
(3,'mentor','098','mentor'),
(4,'\"++\"','\"++\"','\"++\"'),
(5,'anu@gmail.com','578879454','mentor'),
(6,'anu@gmail.com','9876544333','mentor'),
(7,'aa@gmail.com','9876545677','mentor'),
(8,'amala@gmail.com','987654390','mentor'),
(9,'mentornew','098','mentor'),
(10,'kokachi','123','mentor');

/*Table structure for table `mentor` */

DROP TABLE IF EXISTS `mentor`;

CREATE TABLE `mentor` (
  `mentor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Photo` varchar(50) DEFAULT NULL,
  `DOB` int(11) DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  `Qualification` varchar(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Post` varchar(50) DEFAULT NULL,
  `District` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT 'pending',
  PRIMARY KEY (`mentor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `mentor` */

insert  into `mentor`(`mentor_id`,`login_id`,`Name`,`Photo`,`DOB`,`Gender`,`Qualification`,`Place`,`Post`,`District`,`State`,`Phone`,`Email`,`Status`) values 
(1,1001,'','',0,'','','','','','','','','approved'),
(2,NULL,'','',0,'','','','','','','','','approved'),
(3,NULL,'','',0,'','','','','','','','','rejected'),
(4,NULL,'\"++\"','\"++\"',NULL,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','pending'),
(5,NULL,'\"++\"','\"++\"',NULL,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','pending'),
(6,NULL,'\"++\"','\"++\"',0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','\"++\"','pending'),
(7,NULL,'anu','static/photo/20221105-104332.jpg',2022,'Female','MBBS,MD','kgm','kgm','calicut','kerala','578879454','anu@gmail.com','pending'),
(8,NULL,'anu','static/photo/20221105-112154.jpg',2016,'Female','MBBS,MD','kgm','kgm','calicut','kerala','9876544333','anu@gmail.com','pending'),
(9,NULL,'aaaa','static/photo/20221203-093526.jpg',12,'Female','mbbs','kkd','kkd','kkd','kkd','9876545677','aa@gmail.com','pending'),
(10,8,'amala','static/photo/20221203-094951.jpg',7,'Female','degree','mkm','mkm','kkd','kerala','987654390','amala@gmail.com','pending'),
(11,9,'ghsb changed new','/static/photo/20221203-105351.jpg',23,'Female','plus two','kollam','tvm','kkd','kerala','8765437898','ghsb@gmail.com','pending'),
(12,10,'kokachi','/static/photo/20221206-093416.jpg',30,'Other','ppg','kkd','kkd','kkd','kerala','1234567890','@kokachi.com','pending');

/*Table structure for table `motivation` */

DROP TABLE IF EXISTS `motivation`;

CREATE TABLE `motivation` (
  `Mot_id` int(11) NOT NULL AUTO_INCREMENT,
  `Mentor_loginid` int(11) DEFAULT NULL,
  `User_loginid` int(11) DEFAULT NULL,
  `Motivation` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Mot_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `motivation` */

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `Rate_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_loginid` int(11) DEFAULT NULL,
  `Rating` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Rate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `Req_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_loginid` int(11) DEFAULT NULL,
  `Mentor_loginid` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`Req_id`,`User_loginid`,`Mentor_loginid`,`Date`,`Status`) values 
(1,2,9,'2022-12-03','reject');

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `Review_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_loginid` int(11) DEFAULT NULL,
  `Mentor_loginid` int(11) DEFAULT NULL,
  `Review` varchar(50) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Review_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `review` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Photo` varchar(50) DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Post` varchar(50) DEFAULT NULL,
  `District` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`login_id`,`Name`,`DOB`,`Photo`,`Gender`,`Place`,`Post`,`District`,`State`,`Email`,`Phone`) values 
(1,2,'user','0000-00-00',NULL,'male','gcvfhq','dh','drfr','sd','user','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
