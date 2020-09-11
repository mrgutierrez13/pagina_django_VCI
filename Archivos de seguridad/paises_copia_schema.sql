CREATE TABLE `paises_copy` (
  `pais` int(11) NOT NULL,
  `descripcion` varchar(150) NOT NULL,
  `deszon` varchar(150) DEFAULT NULL,
  `otros` varchar(150) DEFAULT NULL,
  `pais_anb` char(3) DEFAULT NULL,
  `continente` int(10) unsigned NOT NULL DEFAULT '0',
  `pais_sis` char(4) DEFAULT NULL,
  PRIMARY KEY (`pais`),
  KEY `index_anb` (`pais_anb`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
