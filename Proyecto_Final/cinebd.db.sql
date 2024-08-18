-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-08-2024 a las 02:24:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cinebd.db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boletos`
--

CREATE TABLE `boletos` (
  `Codigo` varchar(15) NOT NULL,
  `cliente_id` int(5) DEFAULT NULL,
  `funcion_id` int(10) DEFAULT NULL,
  `precio` varchar(10) DEFAULT NULL,
  `asiento` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `boletos`
--

INSERT INTO `boletos` (`Codigo`, `cliente_id`, `funcion_id`, `precio`, `asiento`) VALUES
('', 1, 1, NULL, 'A2'),
('321', 2, 1, '50', ''),
('354', 4, 2, '100', ''),
('B003', 1, 1, '150.0', ''),
('B004', 1, 1, '150.0', ''),
('B005', 1, 1, '150.0', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `ID_Cliente` int(5) NOT NULL,
  `Nombre` tinytext DEFAULT NULL,
  `Apellidos` tinytext DEFAULT NULL,
  `edad` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`ID_Cliente`, `Nombre`, `Apellidos`, `edad`) VALUES
(0, 'Angel', 'Ocampo Franco', 20),
(1, 'Jose', 'Hernandez Dominguez', 25),
(2, 'Sebastian ', 'Hernandez Gonzalez', 18),
(3, 'Gabriel', 'Fernandez Feliz', 22),
(4, 'Valeria', 'Ortega Ocampo', 17),
(5, 'Pablo', 'Sanchez', 20),
(10, 'Juan', 'Hernandez', 18);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comprasdulceria`
--

CREATE TABLE `comprasdulceria` (
  `ID_Prod` int(11) NOT NULL,
  `clientes_id` int(5) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funciones`
--

CREATE TABLE `funciones` (
  `ID_Funcion` int(10) NOT NULL,
  `hora` time DEFAULT NULL,
  `sala_id` int(10) DEFAULT NULL,
  `pelicula_id` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `funciones`
--

INSERT INTO `funciones` (`ID_Funcion`, `hora`, `sala_id`, `pelicula_id`) VALUES
(1, '18:00:00', 1, 1),
(2, '22:30:00', 7, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

CREATE TABLE `peliculas` (
  `ID_Pelicula` int(5) NOT NULL,
  `titulo` tinytext DEFAULT NULL,
  `Duracion` varchar(15) DEFAULT NULL,
  `Geneto` tinytext DEFAULT NULL,
  `Director` varchar(45) DEFAULT NULL,
  `Clasificacion` varchar(35) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `peliculas`
--

INSERT INTO `peliculas` (`ID_Pelicula`, `titulo`, `Duracion`, `Geneto`, `Director`, `Clasificacion`) VALUES
(1, 'Deadpool', '02:00hrs', 'Accion', 'Shawn Levy', 'R'),
(2, 'Intensamente', '02:01hrs', 'Comedia', 'Pete Docker', 'PG'),
(3, 'Mi villano Favorito', '01:35hrs', 'Comedia', 'Pierre Coffin', 'PG'),
(4, 'La Noche del demonio', '01:43hrs', 'Terror', 'James Wan', 'PG-13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `ID` int(5) NOT NULL,
  `Nombre` tinytext DEFAULT NULL,
  `Apellidos` tinytext DEFAULT NULL,
  `Edad` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`ID`, `Nombre`, `Apellidos`, `Edad`) VALUES
(10, 'Francisco', 'Silva Robles', 33),
(11, 'Gerardo', 'Tinoco Cruz', 41),
(12, 'Tomas', 'Ortega Mendez', 22);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `ID_Producto` int(10) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Precio` decimal(11,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`ID_Producto`, `Nombre`, `Precio`) VALUES
(1, 'Palomitas', 50),
(2, 'Refresco', 35),
(3, 'ICEE', 60),
(4, 'Nachos', 65);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salas`
--

CREATE TABLE `salas` (
  `ID_Sala` int(10) NOT NULL,
  `Numero` int(4) DEFAULT NULL,
  `Capacidad` int(5) DEFAULT NULL,
  `Tipo` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `salas`
--

INSERT INTO `salas` (`ID_Sala`, `Numero`, `Capacidad`, `Tipo`) VALUES
(1, 1, 50, 'Clasica'),
(2, 2, 50, 'Clasica'),
(3, 3, 50, 'Clasica'),
(4, 4, 35, 'Clasica'),
(5, 5, 40, 'Clasica'),
(6, 6, 100, 'Premium'),
(7, 7, 100, 'Premium'),
(8, 8, 110, 'Premium'),
(9, 9, 150, 'Premium');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `boletos`
--
ALTER TABLE `boletos`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `funcion_id` (`funcion_id`),
  ADD KEY `cliente_id` (`cliente_id`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID_Cliente`);

--
-- Indices de la tabla `comprasdulceria`
--
ALTER TABLE `comprasdulceria`
  ADD PRIMARY KEY (`ID_Prod`),
  ADD KEY `clientes_id` (`clientes_id`);

--
-- Indices de la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD PRIMARY KEY (`ID_Funcion`),
  ADD KEY `sala_id` (`sala_id`),
  ADD KEY `pelicula_id` (`pelicula_id`);

--
-- Indices de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`ID_Pelicula`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`ID_Producto`);

--
-- Indices de la tabla `salas`
--
ALTER TABLE `salas`
  ADD PRIMARY KEY (`ID_Sala`),
  ADD UNIQUE KEY `Numero` (`Numero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `ID_Producto` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `boletos`
--
ALTER TABLE `boletos`
  ADD CONSTRAINT `boletos_ibfk_1` FOREIGN KEY (`funcion_id`) REFERENCES `funciones` (`ID_Funcion`),
  ADD CONSTRAINT `boletos_ibfk_2` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`ID_Cliente`);

--
-- Filtros para la tabla `comprasdulceria`
--
ALTER TABLE `comprasdulceria`
  ADD CONSTRAINT `comprasdulceria_ibfk_1` FOREIGN KEY (`clientes_id`) REFERENCES `clientes` (`ID_Cliente`);

--
-- Filtros para la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD CONSTRAINT `funciones_ibfk_1` FOREIGN KEY (`sala_id`) REFERENCES `salas` (`ID_Sala`),
  ADD CONSTRAINT `funciones_ibfk_2` FOREIGN KEY (`pelicula_id`) REFERENCES `peliculas` (`ID_Pelicula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
