CREATE TABLE `informacion_proveedor_copia2` (
  `nit_cit` varchar(11) COLLATE utf8_bin NOT NULL,
  `razon_social` varchar(150) COLLATE utf8_bin NOT NULL,
  `tipo_empresa` varchar(1) COLLATE utf8_bin NOT NULL,
  `tipo_societario` varchar(2) COLLATE utf8_bin NOT NULL,
  `nombre_contacto` varchar(80) COLLATE utf8_bin NOT NULL,
  `celular` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  `email_contacto` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `fax` varchar(13) COLLATE utf8_bin DEFAULT NULL,
  `telefono` varchar(7) COLLATE utf8_bin DEFAULT NULL,
  `municipio` varchar(45) COLLATE utf8_bin NOT NULL,
  `zona` varchar(100) COLLATE utf8_bin NOT NULL,
  `domicilio` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`nit_cit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
