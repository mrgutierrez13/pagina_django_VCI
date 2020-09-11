LOAD DATA INFILE 'proveedores_actividad.txt' INTO TABLE proveedores_actividad
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;