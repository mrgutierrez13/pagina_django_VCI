CREATE TABLE `paises` (
  `pais` int(11) NOT NULL,
  `descripcion` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `deszon` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `otros` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pais_anb` char(3) CHARACTER SET utf8 DEFAULT NULL,
  `continente` int(10) unsigned NOT NULL DEFAULT '0',
  `pais_sis` char(4) CHARACTER SET utf8 DEFAULT NULL,
  `acuerdo` varchar(30) COLLATE utf8_unicode_ci NOT NULL DEFAULT '-',
  `rep_diplomatico` varchar(15) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'No',
  PRIMARY KEY (`pais`),
  KEY `index_anb` (`pais_anb`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
