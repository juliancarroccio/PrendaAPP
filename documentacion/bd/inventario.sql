/*
SQLyog Trial v13.1.5  (64 bit)
MySQL - 5.7.24 : Database - dbappscanner
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbappscanner` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `dbappscanner`;

/*Table structure for table `color` */

DROP TABLE IF EXISTS `color`;

CREATE TABLE `color` (
  `id_color` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_color` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_color`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `color` */

insert  into `color`(`id_color`,`descripcion_color`) values 
(1,'Varios'),
(2,'Negro'),
(3,'Blanco'),
(4,'Azul'),
(5,'Amarillo'),
(6,'Rojo'),
(7,'Verde');

/*Table structure for table `familia` */

DROP TABLE IF EXISTS `familia`;

CREATE TABLE `familia` (
  `id_familia` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_familia` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_familia`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `familia` */

insert  into `familia`(`id_familia`,`descripcion_familia`) values 
(1,'Chombas'),
(2,'Carteras'),
(3,'Pantalones Casuales'),
(4,'Pantalones Formales'),
(5,'Camisas'),
(6,'Ropa Interior');

/*Table structure for table `industria` */

DROP TABLE IF EXISTS `industria`;

CREATE TABLE `industria` (
  `id_industria` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_industria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_industria`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `industria` */

insert  into `industria`(`id_industria`,`descripcion_industria`) values 
(1,'Argentina'),
(2,'EEUU'),
(3,'Uruguaya'),
(4,'China');

/*Table structure for table `marca` */

DROP TABLE IF EXISTS `marca`;

CREATE TABLE `marca` (
  `id_marca` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_marca` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_marca`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `marca` */

insert  into `marca`(`id_marca`,`descripcion_marca`) values 
(1,'Columbia'),
(2,'Kevingston'),
(3,'Lacoste'),
(4,'Viamo'),
(5,'Levis'),
(6,'Zara');

/*Table structure for table `producto` */

DROP TABLE IF EXISTS `producto`;

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `id_marca` int(11) DEFAULT NULL,
  `id_proveedor` int(11) DEFAULT NULL,
  `id_industria` int(11) DEFAULT NULL,
  `id_color` int(11) DEFAULT NULL,
  `id_talle` int(11) DEFAULT NULL,
  `id_familia` int(11) DEFAULT NULL,
  `codigoBarra` int(11) DEFAULT NULL,
  `descripcion_producto` varchar(1000) DEFAULT NULL,
  `precio` double NOT NULL,
  `stock` int(11) NOT NULL,
  `iva` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `idx_marca_idx` (`id_marca`),
  KEY `idx_proveedor_idx` (`id_proveedor`),
  KEY `idx_industria_idx` (`id_industria`),
  KEY `idx_color_idx` (`id_color`),
  KEY `idx_talle_idx` (`id_talle`),
  KEY `idx_familia_idx` (`id_familia`),
  CONSTRAINT `idx_color` FOREIGN KEY (`id_color`) REFERENCES `color` (`id_color`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idx_familia` FOREIGN KEY (`id_familia`) REFERENCES `familia` (`id_familia`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idx_industria` FOREIGN KEY (`id_industria`) REFERENCES `industria` (`id_industria`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idx_marca` FOREIGN KEY (`id_marca`) REFERENCES `marca` (`id_marca`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idx_proveedor` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `idx_talle` FOREIGN KEY (`id_talle`) REFERENCES `talle` (`id_talle`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `producto` */

insert  into `producto`(`id_producto`,`id_marca`,`id_proveedor`,`id_industria`,`id_color`,`id_talle`,`id_familia`,`codigoBarra`,`descripcion_producto`,`precio`,`stock`,`iva`) values 
(1,1,1,1,1,4,1,9113245,'Chomba Casual Verde',650,8,21),
(2,4,2,2,2,1,2,9116754,'Cartera Animal Print',1580,4,21),
(3,2,2,1,5,3,3,9119321,'Pantalon Capri',1840,10,21),
(4,3,2,1,4,4,3,9117431,'Pantalon Oxford',860,3,21);

/*Table structure for table `proveedor` */

DROP TABLE IF EXISTS `proveedor`;

CREATE TABLE `proveedor` (
  `id_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_proveedor` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `proveedor` */

insert  into `proveedor`(`id_proveedor`,`descripcion_proveedor`) values 
(1,'Compra Propia'),
(2,'Distribuidora del Sur'),
(3,'El Dorado'),
(4,'Industrias Inteligentes');

/*Table structure for table `talle` */

DROP TABLE IF EXISTS `talle`;

CREATE TABLE `talle` (
  `id_talle` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_talle` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id_talle`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `talle` */

insert  into `talle`(`id_talle`,`descripcion_talle`) values 
(1,'N/A'),
(2,'XS'),
(3,'S'),
(4,'M'),
(5,'L'),
(6,'XL');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
