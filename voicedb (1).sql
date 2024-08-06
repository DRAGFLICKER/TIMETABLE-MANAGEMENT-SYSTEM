/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - voice_project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`voice_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `voice_project`;

/*Table structure for table `apkchecks` */

DROP TABLE IF EXISTS `apkchecks`;

CREATE TABLE `apkchecks` (
  `apkcheck_id` int(11) NOT NULL AUTO_INCREMENT,
  `apk` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`apkcheck_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `apkchecks` */

insert  into `apkchecks`(`apkcheck_id`,`apk`) values 
(3,'Check Android');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'ufhff','hfhffff','users'),
(3,'u','u','users');

/*Table structure for table `pin` */

DROP TABLE IF EXISTS `pin`;

CREATE TABLE `pin` (
  `pin_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `pin` */

insert  into `pin`(`pin_id`,`user_id`,`pin`) values 
(1,1,'1234');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`place`,`phone`,`email`) values 
(1,3,'gug','hchch','hchchc','9874563210','shemi96ven@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
