-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-04-2025 a las 18:14:20
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestferias`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `nombre` varchar(80) NOT NULL,
  `descripcion` text NOT NULL,
  `tlf` varchar(50) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `admin`
--

INSERT INTO `admin` (`id`, `nombre`, `descripcion`, `tlf`, `usuario_id`) VALUES
(1, 'Manuel', 'Administrador de fiestas', '982948574', 1),
(2, 'Pepe', 'Administrador de publicidades', '333333333', 43);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ayuntamiento`
--

CREATE TABLE `ayuntamiento` (
  `id` int(11) NOT NULL,
  `municipio` varchar(256) NOT NULL,
  `descripcion` text NOT NULL,
  `provincia` varchar(256) NOT NULL,
  `comunidad_autonoma` varchar(256) NOT NULL,
  `tlf` varchar(50) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `latitud` float DEFAULT NULL,
  `longitud` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ayuntamiento`
--

INSERT INTO `ayuntamiento` (`id`, `municipio`, `descripcion`, `provincia`, `comunidad_autonoma`, `tlf`, `usuario_id`, `latitud`, `longitud`) VALUES
(2, 'Sevilla', 'Ayuntamiento de Sevilla', 'Sevilla', 'Andalucía', '8888888888', 5, 37.3886, -5.99534),
(3, 'Fregenal de La Sierra', 'Ayuntamiento de la localidad de Fregenal de la Sierra', 'Badajoz', 'Extremadura', '777777777', 6, 38.1664, -6.65258),
(7, 'Cumbres Mayores', 'Ayuntamiento de Cumbres Mayores', 'Huelva', 'Andalucía', '3333333333', 11, 38.0623, -6.64662),
(8, 'Arahal', 'Ayuntamiento de la localidad de Arahal', 'Sevilla', 'Andalucía', '982748574', 12, 37.2624, -5.54493),
(9, 'Hinojales', 'Ayuntamiento de la localidad de Hinojales', 'Huelva', 'Andalucía', '8888888888', 13, 38.0079, -6.58822),
(10, 'Cumbres De Enmedio', 'Ayuntamiento de Cumbres de Enmedio', 'Huelva', 'Andalucía', '2222222222', 15, 38.0731, -6.69351),
(11, 'Paterna de Rivera', 'Ayuntamiento de la localidad de Paterna de Rivera', 'Cádiz', 'Andalucía', '3333333333', 16, 36.523, -5.8647),
(12, 'Arcos de la Frontera', 'Ayuntamiento de Arcos de la Frontera y Delegación Municipal de Jédula', 'Cádiz', 'Andalucía', '8888888888', 17, 36.7527, -5.81221),
(13, 'Villarrodrigo', 'Ayuntamiento de Villarrodrigo y Delegación Municipal de Onsares', 'Jaén', 'Andalucía', '982748574', 18, 38.4873, -2.63637),
(14, 'Almería', 'Ayuntamiento de la ciudad capital de provincia, Almería', 'Almería', 'Andalucía', '666666666', 28, 36.8414, -2.46281),
(15, 'Antequera', 'Ayuntamiento de la localidad malagueña de Antequera', 'Málaga', 'Andalucía', '888888888', 29, 37.0184, -4.55966),
(16, 'Burriana', 'Ayuntamiento de la localidad de Burriana', 'Castellón', 'Valencia', '444333222', 30, 39.8877, -0.0846321),
(17, 'Ceuta', 'Ayuntamiento de la ciudad autónoma de Ceuta', 'Ceuta', 'Ceuta', '111111111', 31, 35.8944, -5.35582),
(18, 'Granada', 'Ayuntamiento de la ciudad de Granada', 'Granada', 'Andalucía', '123456789', 32, 37.1735, -3.59953),
(19, 'Línea de la Concepción', 'Ayuntamiento de la localidad Gaditana de La Línea', 'Cádiz', 'Andalucía', '777777777', 33, 36.1583, -5.34047),
(20, 'Lucena', 'Ayuntamiento de la localidad Cordobesa de Lucena', 'Córdoba', 'Andalucía', '222222222', 34, 37.4091, -4.48601),
(21, 'Fuentes de León', 'Ayuntamiento de la localidad de Fuentes de León', 'Badajoz', 'Extremadura', '666666666', 35, 38.0681, -6.54022),
(22, 'La Rinconada', 'Ayuntamiento de la localidad de La Rinconada', 'Sevilla', 'Andalucía', '888888888', 36, 37.4867, -5.98149),
(23, 'San Juan del Puerto', 'Ayuntamiento de la localidad Onubenses de San Juan del Puerto', 'Huelva', 'Andalucía', '777777777', 38, 37.3142, -6.84078),
(24, 'La Puebla Del Río', 'Ayuntamiento de la localidad Sevillana de La Puebla del Río', 'Sevilla', 'Andalucía', '123456789', 39, 37.2698, -6.06272),
(25, 'Chiclana de la Frontera', 'Ayuntamiento de la localidad de Chiclana de la Frontera', 'Cádiz', 'Andalucía', '222222222', 40, 36.4191, -6.14607),
(26, 'Alcalá de Guadaíra', 'Ayuntamiento de la localidad Sevillana de Alcalá de Guadaíra', 'Sevilla', 'Andalucía', '444333222', 44, 37.3398, -5.84084);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `feriante`
--

CREATE TABLE `feriante` (
  `id` int(11) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `descripcion` text NOT NULL,
  `tlf` varchar(50) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `feriante`
--

INSERT INTO `feriante` (`id`, `nombre`, `tipo`, `descripcion`, `tlf`, `usuario_id`) VALUES
(2, 'Atracciones Guillen', 'Atracciones', 'Empresa de atracciones que cuenta con \"Atracción Canguro Saltinvanquis\" y \"Atracción El Tren de la Bruja\"', '777777777', 14),
(3, 'Churrería Ana Belén', 'Comida', 'Churrería y cafetería Ana Belén', '982748574', 27),
(4, 'Atriculos Paco', 'Artículos', 'Empresa de venta de juguetes y artículos de regalo con flota de 4 puestos ', '344522167', 45),
(5, 'Atracciones Millán', 'Atracciones', 'Empresa de atracciones que cuenta con \"Atracción Coches Locos\" y \"Atracción Tiovivo\"', '222222220', 46);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fiesta`
--

CREATE TABLE `fiesta` (
  `id` int(11) NOT NULL,
  `idAyun` int(11) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFin` date NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fiesta`
--

INSERT INTO `fiesta` (`id`, `idAyun`, `fechaInicio`, `fechaFin`, `nombre`, `descripcion`) VALUES
(2, 6, '2025-09-08', '2025-09-09', 'Salud', 'Fiestas en Honor a la Virgen de la Salud'),
(3, 5, '2025-10-23', '2025-11-15', 'Festival de las Naciones', 'Festival Internacional de Cultura y Tradiciones'),
(7, 13, '2025-04-30', '2025-05-03', 'Tórtola', 'Fiestas Patronales de la Virgen de Tórtola'),
(8, 12, '2025-09-05', '2025-09-08', 'Feria del Verdeo', 'Fiestas Grandes en conmemoración de la recolección de la aceituna'),
(9, 15, '2025-06-27', '2025-06-30', 'San Pedro', 'Fiestas en honor al Patrón del pueblo'),
(10, 16, '2025-06-12', '2025-06-16', 'Feria de la Primavera', 'Feria del Toro y Fiestas de la Primavera'),
(11, 17, '2025-05-22', '2025-05-25', 'Feria de Jédula', 'Fiestas Grandes del municipio'),
(13, 18, '2025-05-23', '2025-05-25', 'Feria de Onsares', 'Fiestas Grandes de nuestra pedanía Onsares'),
(14, 11, '2025-06-18', '2025-06-23', 'Corpus Christi', 'Tradicionales Fiestas del Corpus Christi'),
(15, 28, '2025-08-16', '2025-08-24', 'Feria de Almería', 'Feria de Almería, que se celebra del 16 al 24 de agosto en honor a su patrona la Virgen del Mar.'),
(16, 29, '2025-05-30', '2025-06-01', 'Feria de Primavera', 'Los orígenes de esta feria se remontan muy atrás, a 1855.\r\nLo que hace tan interesante a esta feria es que ha conservado parte de su función original, que era la de lugar de compra-venta de ganado.\r\nEl aspecto agropecuario de esta feria se mantiene, con su mercado de productos de la tierra y sus numerosos talleres en torno a la cabra malagueña. Con esta raza autóctona se elaboran los famosos quesos de la región.'),
(17, 30, '2025-05-23', '2025-06-01', 'Virgen de los Desamparados', 'Fiestas en Honor a la Virgen de los Desamparados'),
(18, 31, '2025-07-29', '2025-08-05', 'Feria de Ceuta', 'Serán días en los que aunar la diversión y el civismo, la tolerancia y las ganas de pasarlo bien en una cordial convivencia para vivir nuestras Fiestas Patronales como siempre: en las casetas, con la familia y los amigos, en las atracciones, participando en las tómbolas, acompañando a la Patrona y disfrutando de estos ocho días como siempre hemos sabido hacerlo.'),
(19, 32, '2025-06-14', '2025-06-21', 'Feria del Corpus', 'Corpus de Granada se celebrará desde el sábado 14 de junio hasta el 21 de junio de 2025, lo que suponen tres semanas más tarde que cuando lo ha hecho en 2024.\r\nAdemás, el Jueves de Corpus será el 19 de junio de 2025, fecha a partir de la que se celebran los días grandes, que comienzan con la salida de la Tarasca el miércoles 18 de junio.\r\nEl encendido del alumbrado tendrá lugar el sábado 14 de junio en la portada del Recinto Ferial, mientras la despedida con los tradicionales fuegos artificiales'),
(20, 33, '2025-07-11', '2025-07-20', 'Feria y Velada de La Línea', 'Siendo casi la única fiesta de los alrededores sin origen ganadero, la Feria de La Línea conmemora el nacimiento de la ciudad. Del 11 al 20 de julio la ciudad se viste de faralaes y se engalana con farolillos y volantes para celebrar su fiesta por antonomasia.\r\nLa alegría, la diversión, la amistad y la buena se dan cita en el Recinto Ferial.\r\nLa Velada y Fiestas de La Línea ha sido declarada de Interés Turístico de Andalucía.'),
(21, 34, '2025-05-02', '2025-05-05', 'Feria Aracelitanas', 'Muchos actos conmemorativos que se festejan: la proclamación de la reina de las Fiestas Aracelitanas, una multitudinaria ofrenda de flores amenizada con un pasacalles y con los trajes típicos que visten las mujeres o la procesión de la imagen por la ciudad hasta su entrada en la Parroquia de San Mateo acompañada por fuegos artificiales. El primer domingo de junio llega la despedida a la Virgen, con la Romería de Subida al Santuario. '),
(22, 35, '2025-06-17', '2025-06-22', 'Corpus Christi ', 'Fiestas Grandes del Corpus Christi'),
(23, 36, '2025-06-05', '2025-06-08', 'La Feria del Abrazo', 'La Feria del Abrazo de La Rinconada se realiza en el recinto multiusos \"El Abrazo\"'),
(24, 38, '2025-06-18', '2025-06-24', 'Fiestas de San Juan', 'Fiestas patronales en San Juan del Puerto (Huelva), que tienen lugar del 18 al 24 de junio en honor a San Juan Bautista (24 de junio). Una semana de fiestas que comienza el día 18 con la coronación de la reina y termina el 24 de junio con la festividad de San Juan.'),
(25, 39, '2025-06-18', '2025-06-22', 'Feria del Corpus Christi', 'La fiesta más celebrada en La Puebla del Río es el Corpus Christi. Esa semana es considerada la «semana grande» pues tiene también lugar estos días la Feria, considerada de gran prestigio.'),
(26, 40, '2025-06-11', '2025-06-15', 'Feria de San Antonio', 'Vinculada en su origen a una antigua feria ganadera , mantiene testimonialmente este carácter, si bien, se ha convertido en la fiesta más representativa de la ciudad que vive esos días entre el bullicio multicolor de los trajes típicos y los bailes por sevillanas , siendo el vino fino de Chiclana elemento obligado en las reuniones de las casetas, que se convierten en la práctica, en segundo hogar durante la feria.'),
(27, 11, '2025-12-05', '2025-12-08', 'Jonadas Gastronómicas', 'Feria Gastronómico-Cultural \'Saborea Cumbres Mayores\"'),
(28, 44, '2025-05-29', '2025-06-01', 'Feria de Alcalá', 'Tradicional feria de Alcalá de Guadaíra');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fiesta_parcela`
--

CREATE TABLE `fiesta_parcela` (
  `fiesta_id` int(11) NOT NULL,
  `parcela_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fiesta_parcela`
--

INSERT INTO `fiesta_parcela` (`fiesta_id`, `parcela_id`) VALUES
(3, 7),
(9, 26),
(9, 27),
(9, 28),
(9, 29),
(10, 32),
(14, 5),
(14, 11),
(14, 12),
(14, 13),
(14, 14),
(14, 15),
(14, 16),
(14, 17),
(14, 19),
(14, 20),
(14, 21),
(14, 22),
(14, 23),
(23, 31),
(27, 18),
(27, 24),
(27, 25),
(28, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parcela`
--

CREATE TABLE `parcela` (
  `id` int(11) NOT NULL,
  `idAyun` int(11) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `localizacion` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`localizacion`)),
  `detalles` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `parcela`
--

INSERT INTO `parcela` (`id`, `idAyun`, `nombre`, `tipo`, `localizacion`, `detalles`) VALUES
(5, 11, 'Plaza Esperanza At1', 'Atracciones', '\"[[[-6.642737,38.059985],[-6.642673,38.059869],[-6.642531,38.05996],[-6.642737,38.059985]]]\"', 'tiene pendiente'),
(7, 5, 'Plaza At1', 'Atracciones', '\"[[[-5.991325,37.392828],[-5.991325,37.392962],[-5.991119,37.392962],[-5.991119,37.392828],[-5.991325,37.392828]]]\"', 'tiene pendiente'),
(10, 11, 'Plaza Esperanza C1', 'Comida', '\"[[[-6.643167,38.06013],[-6.643049,38.060132],[-6.643043,38.060005],[-6.643207,38.060003],[-6.643167,38.06013]]]\"', 'Ha de haber una separación para el paso de personas de 1,5 metros entre el puesto y las mesas '),
(11, 11, 'Plaza Esperanza At3', 'Atracciones', '\"[[[-6.642665,38.059745],[-6.642721,38.059785],[-6.642638,38.059844],[-6.642585,38.059804],[-6.642665,38.059745]]]\"', 'tiene un escalón por el acerado'),
(12, 11, 'Plaza Esperanza At2', 'Atracciones', '\"[[[-6.643081,38.059641],[-6.643086,38.059529],[-6.642936,38.059533],[-6.642724,38.059711],[-6.642831,38.059761],[-6.643081,38.059641]]]\"', 'tiene pendiente'),
(13, 11, 'Plaza Esperanza At4', 'Atracciones', '\"[[[-6.643279,38.059523],[-6.643279,38.05961],[-6.643118,38.05961],[-6.643118,38.059523],[-6.643279,38.059523]]]\"', 'tiene pendiente'),
(14, 11, 'Plaza Esperanza Ar1', 'Atracciones', '\"[[[-6.643268,38.060038],[-6.643268,38.060091],[-6.643242,38.060091],[-6.643242,38.060038],[-6.643268,38.060038]]]\"', 'parcela de 15 m2'),
(15, 11, 'Plaza Esperanza Ar2', 'Atracciones', '\"[[[-6.643271,38.059974],[-6.643271,38.060025],[-6.643242,38.060025],[-6.643242,38.059974],[-6.643271,38.059974]]]\"', '15 m2'),
(16, 11, 'Plaza Esperanza Ar3', 'Artículos', '\"[[[-6.643287,38.05978],[-6.643287,38.059835],[-6.64326,38.059835],[-6.64326,38.05978],[-6.643287,38.05978]]]\"', '15 m2'),
(17, 11, 'Plaza Esperanza Ar4', 'Artículos', '\"[[[-6.643293,38.059674],[-6.643293,38.059748],[-6.643268,38.059748],[-6.643268,38.059674],[-6.643293,38.059674]]]\"', '16 m2'),
(18, 11, 'Plaza Esperanza CM', 'Otros', '\"[[[-6.643016,38.060125],[-6.643016,38.060047],[-6.642595,38.060034],[-6.642609,38.060154],[-6.642802,38.060163],[-6.643016,38.060125]]]\"', 'carpa municipal con cocina'),
(19, 11, 'Plaza Esperanza C2', 'Comida', '\"[[[-6.642542,38.059844],[-6.642574,38.059865],[-6.642496,38.059929],[-6.642456,38.05991],[-6.642542,38.059844]]]\"', ''),
(20, 11, 'Plaza Esperanza At5', 'Atracciones', '\"[[[-6.643129,38.059971],[-6.643126,38.059863],[-6.642931,38.059918],[-6.642998,38.059983],[-6.643129,38.059971]]]\"', 'terreno de arena'),
(21, 11, 'Plaza Esperanza Ar5', 'Artículos', '\"[[[-6.643392,38.060178],[-6.643392,38.060197],[-6.643306,38.060197],[-6.643306,38.060178],[-6.643392,38.060178]]]\"', '18 m2'),
(22, 11, 'Plaza Esperanza Ar6', 'Artículos', '\"[[[-6.643636,38.060191],[-6.643636,38.060208],[-6.643539,38.060208],[-6.643539,38.060191],[-6.643636,38.060191]]]\"', '18 m2'),
(23, 11, 'Plaza Esperanza Ar7', 'Artículos', '\"[[[-6.643786,38.0602],[-6.643786,38.060219],[-6.643684,38.060219],[-6.643684,38.0602],[-6.643786,38.0602]]]\"', '18 m2'),
(24, 11, 'Plaza Portugal', 'Comida', '\"[[[-6.646623,38.063697],[-6.64659,38.063704],[-6.646574,38.063628],[-6.646612,38.063619],[-6.646623,38.063697]]]\"', 'Barra de la salida de la Plaza de Toros'),
(25, 11, 'Paseo Andalucia CM', 'Otros', '\"[[[-6.644112,38.061461],[-6.643954,38.061303],[-6.643873,38.061377],[-6.643962,38.061442],[-6.64393,38.06147],[-6.643978,38.061499],[-6.644021,38.06147],[-6.64405,38.061503],[-6.644112,38.061461]]]\"', 'Caseta Principal con escenario y barra'),
(26, 15, 'C. Colón At1', 'Atracciones', '\"[[[-6.693073,38.072094],[-6.692936,38.072075],[-6.692926,38.072119],[-6.693057,38.072132],[-6.693073,38.072094]]]\"', 'Tiene leve pendiente'),
(27, 15, 'C. del Pozo CM', 'Otros', '\"[[[-6.692867,38.072057],[-6.692888,38.071821],[-6.692783,38.071821],[-6.692775,38.072062],[-6.692867,38.072057]]]\"', 'Caseta Municipal con servicio de barra y escenario'),
(28, 15, 'C. Colón At2', 'Atracciones', '\"[[[-6.693229,38.072161],[-6.693245,38.072121],[-6.693132,38.072095],[-6.693119,38.07214],[-6.693229,38.072161]]]\"', 'Terreno con leve desnivel'),
(29, 15, 'A. Andalucia C1', 'Comida', '\"[[[-6.692515,38.072332],[-6.692499,38.072296],[-6.692402,38.072324],[-6.692424,38.072353],[-6.692515,38.072332]]]\"', 'Terreno llano de 20m2 para puesto de comida'),
(30, 44, 'P. Central At1', 'Atracciones', '\"[[[-5.838807,37.340412],[-5.838705,37.340221],[-5.838394,37.340336],[-5.838555,37.340528],[-5.838807,37.340587],[-5.838807,37.340412]]]\"', 'Terreno llano de arena, 40 m2'),
(31, 36, 'Abrazo At1', 'Atracciones', '\"[[[-5.962393,37.480343],[-5.962323,37.480522],[-5.962183,37.480471],[-5.962178,37.480364],[-5.962275,37.4803],[-5.962393,37.480343]]]\"', 'Terreno asfaltado con leve desnivel, 32m2'),
(32, 16, 'Julio Díez At1', 'Atracciones', '\"[[[-5.87521,36.526306],[-5.87521,36.526362],[-5.87515,36.526362],[-5.87515,36.526306],[-5.87521,36.526306]]]\"', 'Terreno llano asfaltado (incluye acerados), 35 m2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicidad`
--

CREATE TABLE `publicidad` (
  `id` int(11) NOT NULL,
  `idPublicitado` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `foto` varchar(256) NOT NULL,
  `codigo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `publicidad`
--

INSERT INTO `publicidad` (`id`, `idPublicitado`, `fecha`, `foto`, `codigo`) VALUES
(3, 3, '2025-07-13', 'IMG_20211123_153531_506.jpg', 'T1C6NYE4BR'),
(18, 2, '2025-07-20', 'IMG_20180320_234950_675.jpg', '4MD22QDHWK'),
(22, 19, '2025-08-22', 'IMG_20190111_145125_015.jpg', 'K626XX5XGC'),
(23, 20, '2025-06-23', '358598889_2514654842031779_2117678657483876510_n.jpg', '40BEY994D2'),
(24, 21, '2025-06-23', 'IMG_20231017_195257_625.jpg', '5JQPF5MI6T'),
(26, 22, '2025-06-23', 'Captura_de_pantalla_2025-03-04_100436.png', 'X7JJ0XKYO1'),
(27, 23, '2025-06-23', 'Captura_de_pantalla_2025-03-04_102252.png', 'EI6MJ2WFTX'),
(28, 24, '2025-06-23', 'Captura_de_pantalla_2025-03-04_131547.png', 'FXEMCH9O9P'),
(29, 25, '2025-07-03', '47684788n.jpg', 'V5YEVWGD5S'),
(30, 26, '2025-03-05', '7788932550901608927_n.jpg', 'GQH2SD3DKB'),
(31, 37, '2025-07-04', 'Captura_de_pantalla_2025-04-05_123210.png', 'LNM0JAW6D9'),
(32, 41, '2025-07-04', 'Captura_de_pantalla_2025-04-02_134413.png', 'C11BYSW89O'),
(33, 42, '2025-10-02', 'Captura_de_pantalla_2025-04-05_131802.png', 'HC3LN3G6RC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicitado`
--

CREATE TABLE `publicitado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(256) NOT NULL,
  `descripcion` text NOT NULL,
  `tlf` varchar(50) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `publicitado`
--

INSERT INTO `publicitado` (`id`, `nombre`, `descripcion`, `tlf`, `usuario_id`) VALUES
(1, 'MeCamela', 'Orquesta tributo a Camela con más de 20 años de experiencia, perfecta para verbenas y ferias', '777777777', 2),
(2, 'Trío Fantasía', 'Trío musical Fantasía, contamos con un amplio repertorio musical desde música de los 80\'s hasta los últimos éxitos.', '8888888888', 3),
(3, 'Circo Saltimanqui', 'Circo Saltimbanqui es un pequeño circo de Hnos. Parada que ambula de pueblo en pueblo. En invierno va con su carpa mientras que en verano circulan al aire libre.', '3333333333', 19),
(4, 'Banda Tributo a Zeppelin', 'Banda de música tributo a Zeppelin, compuesta por 5 músicos con un gran potencial: Fran (Bateria), Alex (Guitarra), Arnau (Voz), Ricard (Bajo) y Jota (Teclado) que han escuchado Rock&Roll desde donde les alcanza la memoria, y influenciados de forma indudable por los gigantes LED ZEPPELIN.', '999999999', 20),
(5, 'Los Cassettes', '📼💘 Grupo de pop rock tinerfeño\r\n✨Ganadores del Alisios Festival Pop 2022✨', '111111111', 21),
(6, 'El Sur A Cuerpo Limpio', 'Portal de Festejos Taurinos Populares del Sur de la Península Ibérica', '123456789', 22),
(7, 'Pepe Torres FPV', 'Piloto profesional FPV (drones) #freestyle #Cinematic', '8888888888', 23),
(8, 'Mawi Banda Soriano', 'Dj animador para celebraciones, verbenas y todo tipo de eventos', '982748574', 24),
(9, 'Ana Moreno', 'Cantante de Pop, flamenco y rumba con acompañamiento de guitarra y cajón', '3333333333', 25),
(10, 'Racso Music', 'Dj animador', '8888888888', 26),
(11, 'RUMBITA SHOWMAN', 'ShowMan - Speaker - Animador - DJ - Artista - Músico - Pianista - Percusionista - Manager - Técnico de sonido - Profe de zumba... Etc.', '777777777', 37),
(12, 'Pirotecnia Virgen de las Nieves', 'Pirotecnia Virgen de las Nieves da servicio a muchas facetas de la vida del espectáculo, conforme a nuestra filosofía del servicio al cliente, esta pirotecnia provee de fuegos artificiales a Ferias, Fiestas, Romerías y Celebraciones en general, de pueblos de las provincias de Sevilla, Huelva, Cádiz, Córdoba, Málaga y Badajoz principalmente, aunque tenemos infraestructura para desplazarnos a cualquier punto de la geografía española.', '222222222', 41),
(13, 'Dj Kevin', 'DJ Animador de todo tipo de música, experto en actualidad', '333333333', 42);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud`
--

CREATE TABLE `solicitud` (
  `id` int(11) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `fecha` datetime NOT NULL,
  `idFeriante` int(11) NOT NULL,
  `idParcela` int(11) NOT NULL,
  `idFiesta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `solicitud`
--

INSERT INTO `solicitud` (`id`, `estado`, `fecha`, `idFeriante`, `idParcela`, `idFiesta`) VALUES
(6, 'aceptada', '2025-03-01 13:07:39', 14, 7, 3),
(9, 'aceptada', '2025-04-11 11:40:45', 14, 20, 14),
(10, 'rechazada', '2025-04-03 16:55:53', 14, 12, 14),
(11, 'rechazada', '2025-04-11 22:15:19', 14, 13, 14),
(13, 'pendiente', '2025-03-03 22:07:52', 14, 14, 14),
(15, 'aceptada', '2025-04-11 11:32:23', 14, 26, 9),
(16, 'pendiente', '2025-04-11 11:28:31', 14, 30, 28),
(17, 'pendiente', '2025-04-11 11:28:47', 14, 31, 23),
(18, 'pendiente', '2025-04-11 11:28:59', 14, 32, 10),
(19, 'pendiente', '2025-04-11 11:33:09', 27, 29, 9),
(20, 'aceptada', '2025-04-11 11:40:32', 27, 19, 14),
(21, 'pendiente', '2025-04-11 11:54:21', 45, 16, 14),
(22, 'pendiente', '2025-04-11 11:54:33', 45, 21, 14),
(23, 'pendiente', '2025-04-11 11:59:37', 46, 11, 14),
(24, 'pendiente', '2025-04-11 11:59:48', 46, 13, 14);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `email` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `rol` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `email`, `password`, `rol`) VALUES
(1, 'admin@gmail.com', 'scrypt:32768:8:1$iz9VDZSM9DLtW1WI$0f6627747da08c6eaf853a3fe70f33df7fc6cd51f857ddd6e955a056a405dd013e6db7e3c80437ace5ed246ed2e8e41680cf52938e5f387c8f98d950f0402959', 'admin'),
(2, 'mecamela@gmail.com', 'scrypt:32768:8:1$Qt7Td5rWlBtbsmqJ$bf2c4effeb94334bf111b4011ef5f00496adfa7d1c0e805a93c52f74deeb5f2a5ea943b262bf2929d1696682c523dff45e394030d8ad9d5b4c170aa033ebdbd8', 'publicitado'),
(3, 'triofantasia@gmail.com', 'scrypt:32768:8:1$BvqLWGetiNlYqYMN$e925b15a60493650c6f9ba0e3d998a54cbf4dee8a4bd61a9f74ef7e5364d3b15a83254076bd02de60164626494f832f17f664aa22a43e10345896b055111ae3c', 'publicitado'),
(5, 'sevilla@gmail.com', 'scrypt:32768:8:1$IyAPeGuPw6goD3WZ$4355bf6bb97233f386c02ce689a4e7a5bd5c9b6b63bf0269285b3cbeeb99dfd36c8f3884cb6d5533a61ff77c8c7e70eb3f60b95e7640a8d68dfa66f055f422c2', 'ayuntamiento'),
(6, 'fregenaldelasierra@gmail.com', 'scrypt:32768:8:1$n8qYmu2Kz4hDrUn4$e1fdff7d404141197b525dbe21417dcfdfd6b76d469552512c93515f6da119458882cf20fcae342fa17fb3a4257ea58b09854c80955a32c91299416885b6e61b', 'ayuntamiento'),
(11, 'cumbresmayores@gmail.com', 'scrypt:32768:8:1$mWYLpkKgdofSpses$3234c04f6bac418d49ec875e7c3e92b09b69ab0f656a8b21f98672ad784c1d1eebf9fa22ed964d04c8de297234adc11cc39cc42d4ed4176a7b4fdef6f1d7fb31', 'ayuntamiento'),
(12, 'arahal@gmail.com', 'scrypt:32768:8:1$JOn1B7lHVtdCZisR$3fd107bd82004e8e51e12fafec7baec75ebeed7ac9a3e7b80fd58a9b8bc6f2fa2e11c08524053c1e16d421cd1d474c13be915d9e1cbd0dc86e30626b9b568a50', 'ayuntamiento'),
(13, 'hinojales@gmail.com', 'scrypt:32768:8:1$xlBBLq5xHwnoxOAI$8f23216349892769c994c47a8ea81822346551af7eb8ba64f6d0f20cd0877bb81c68125b4115425a06c7c01cee972ac88f1928277ec1532d3dc1e65b335021ee', 'ayuntamiento'),
(14, 'atraccionesguillen@gmail.com', 'scrypt:32768:8:1$ZdsQbQKx595KZpxI$2e3be6cd59812480c0c7de1d43c1e98e467f22a35d20f1708ea20ef0f7d5d0005c2c8acadd5d55ce27c3d2ab874efa808ba98363472ed129b567ee239d5621be', 'feriante'),
(15, 'cumbresdeenmedio@gmail.com', 'scrypt:32768:8:1$gFSBgyZduC5b0H1t$d74117622dbd9b353c0288dbb04b8b081cae7f213e15ed0436ca645ae32098440c42fc5fb814416bd154ac0b7547af69e1c0a07474b056b1701ec61cbb3f0c16', 'ayuntamiento'),
(16, 'paternaderivera@gmail.com', 'scrypt:32768:8:1$61fLHKIzxISi1dWw$146f48a6f1a7ea9b158b619f0a6deb4239a7b10921321ccc74b772eb6706ef56060d3b7675f462a2d1da1fd4da623afcea4e7ecb56b65965b180fec2fc88ef98', 'ayuntamiento'),
(17, 'arcosdelafrontera@gmail.com', 'scrypt:32768:8:1$0GCHlvN3CyBCwJRv$72ef765d1617914f5418b213a27a15022ca3e59a8be18b2217cfd5e8f4991fb856b62fe8891e1f91aef73c59093e16f1cd69bb4be12a298c9e966229985dbd0d', 'ayuntamiento'),
(18, 'villarrodrigo@gmail.com', 'scrypt:32768:8:1$xQ1GqFOl6fBOVsRb$0f9d0f6e7e64e2af4da69e510f031364954d157dfb6eb51e97e1a87b3b49a421866d6096d4bd3369d9754ce40b4e1aceb047567ac06f767fefcc6332c1be9ae1', 'ayuntamiento'),
(19, 'SaltimanquiCirco@gmail.com', 'scrypt:32768:8:1$hZXGnrTxaSD0QHcn$d31308c6b1aae4742acc4e8a5a7e6c53b98be97bb49319adf98a09fc3b48b2a7652758123a2d89987e0efbe8b0e971cfa09ff964ecd08bcf6ab8b2b2add28cdc', 'publicitado'),
(20, 'ZeppelinBand@gmail.com', 'scrypt:32768:8:1$oYh2thQxe0w44wT2$1339df2c29604157d48e60617437f2ae7ce4a5d194dd8dfb697d300f70c043edf3b7d903bc90d73daad80d0ee11422c3f1453ef41a2a6100083a901bc481567b', 'publicitado'),
(21, 'cassettes@gmail.com', 'scrypt:32768:8:1$yWUS1uhWnFmioBXm$432756da8c899c0967dd6454838d4863ba51738366b34900e5a873620bfe355714eebe098de13c242ce636a21d0220e7c3902f8fcad6959f9a10f038f7060102', 'publicitado'),
(22, 'elsuracuerpolimpio@gmail.com', 'scrypt:32768:8:1$1YhJbutxr2Se9g31$f80b2f0350e0c21d4156481c03255bf5853bb02de002d75c21ee7cd7e6e7d91ac058e7b7f6c9f63f5bc53bae099a21331781a6117ab4ecce15acb54fad6f9afb', 'publicitado'),
(23, 'pepetorresfpv@gmail.com', 'scrypt:32768:8:1$7ZYv3AqqpfnWiRMJ$5d0378174f64ac9806de340591e7576b0bc751d7f0f6bf1a44ff242bbda384213f3abcabcfbae7c560a7c6b8b92dc0796f2d560898ff7a74d307a8eae170bb1c', 'publicitado'),
(24, 'mawiSoriano@gmail.com', 'scrypt:32768:8:1$SuSTdE8wKIZkcY1J$b88ba01bec8df0089b49e1b1092319c0ff7c2fc12e9600c5eedaa33160a7e07e133eeca0765ac0eaa5e804d5bc8aad51fe9f45c56462cb4d5c01d13bd4c975e1', 'publicitado'),
(25, 'anamoreno@gmail.com', 'scrypt:32768:8:1$iekfJYMSTEmLfgXB$03f576fefd89925980b9b2eb3458b9faf1c677809a4cadf258c8d1e9e19abc51cc983a875b13848b3ce745d667f80f113c3e36e819d359fe4c7161fc6604f035', 'publicitado'),
(26, 'racsomusic@gmail.com', 'scrypt:32768:8:1$l3Uj5ziiPpL0IyQ0$8bc5f2ed342038b4e4794823170c94e4957e0908048f159b0a7b44e745abff97e1d65598148e976be12f31ef35c818bee171bfee4a3c5a2d41a9337a1fc36816', 'publicitado'),
(27, 'anabelenchurreria@gmail.com', 'scrypt:32768:8:1$eTRFiQ7sFbMOoSq7$26ce1b6f29bd267269ea47aefc7cd60dc885d18d3e726dd52603c1f53db269d5c174b1a73d2e996aa2b39c61c4e57faf6b4d415a205c9f6cad44a078bbf459ac', 'feriante'),
(28, 'almeria@gmail.com', 'scrypt:32768:8:1$h8PYO7hzoD8r9o2L$aa127f30ab9b172599b685ad425c5462a5f3839fd6e3a2604795f5db2902ebfa4c935e8009abb2accc58e6070911db0c27653b4a0baad20e468774df1bf8bcb6', 'ayuntamiento'),
(29, 'antequera@gmail.com', 'scrypt:32768:8:1$wW6GGHn9pkJOYWxH$a4c3a5bbe3f09e2f7d8d02f5059d36494e855264fb74cdbf3d4325ebb0ee4698f7f937287cef8266849f5dbcc2699aca38ac20fd11104fc9399ca117e5532cbe', 'ayuntamiento'),
(30, 'burriana@gmail.com', 'scrypt:32768:8:1$Uh3Nk3SgDqjqTsi8$82833d70d83a3dcdd2a900ab79186cae2e9f38a275e0a24368207c272726818a8cff9f10a5e92dd72b737e9634ab87dde811b15d2dedb63e34e8e87845d4ed68', 'ayuntamiento'),
(31, 'ceuta@gmail.com', 'scrypt:32768:8:1$TdeRbgaRkyEs4Cya$0d1d4d246697f1b19c912b97e6535e519c56d60e30021521a3adce90f1240c7796a38c835d056abc66be19f341c98d812e77ee75cd1f8f950b5dbd6ce9edecb3', 'ayuntamiento'),
(32, 'granada@gmail.com', 'scrypt:32768:8:1$pvnYj1gIwFxiQxIq$168755ac6ac6a187f35384e034ab0d646f05b8a9308f6fdbba0c82560c19182d474cffa370bfe3e03de3ed270b1e0b13173321077d28dd6fa0cfe9271d00aaf1', 'ayuntamiento'),
(33, 'lalinea@gmail.com', 'scrypt:32768:8:1$mw77QzBkHwBsMkRq$3ce8a2900e19b8cd4c0a039d4386be748cd0c978cc745e3f4491aef896604a5820dd0e13329c94c532a52a04cd165f83955db8b7c8eead6cc9fd2ea5d521f197', 'ayuntamiento'),
(34, 'lucena@gmail.com', 'scrypt:32768:8:1$a8dANDbzG7XKmRNk$26598f6cb85545ff3d9812dbd1dd32ba6d2bfd4031c1d74e91e0d1f53f7624644763d5d3a5c55b57673644fa5ab03052f233209fe7e199c79df33a4d4878afa6', 'ayuntamiento'),
(35, 'fuentesdeleon@gmail.com', 'scrypt:32768:8:1$4E8sKu24MSL5P8P8$900bdadd7dd93553742d6b0163724394c57fde66061ee6a5e9aa445645f11b671ca067803bbdf940b0ded7d96ad1c029a5e5f42634257a18ad9e77e5023319c6', 'ayuntamiento'),
(36, 'larinconada@gmail.com', 'scrypt:32768:8:1$AUetLzdkzeNdRIvn$7621e3cde26d1d39417c786bcafddba8b592a4e2c3fa59238ccfc6b8e17319336b4e7a9fa6d445b210cc347f55653f6614c4fa5d0023daf68fd4d45467edfde4', 'ayuntamiento'),
(37, 'rumbitashowman@gmail.com', 'scrypt:32768:8:1$FwuFQzX6lD5p0HHe$a754f7d12038b2f344e1353edc6445e18a5d01547f331fd53733070b67322554b288de90fdb51474e1e53f2c336006ee4d36d54d5482a96eeb0c577d4ad0b892', 'publicitado'),
(38, 'sanjuandelpuerto@gmail.com', 'scrypt:32768:8:1$GC0aEXUacpkcgXzs$83ea80ebc74db0181b0386f5ea7f532b97ef5f72a491aa194ffeb2f8a272b3e22068cacd8722632acfc5ceebf89839e6fd4face476e68d317a340ec354820d06', 'ayuntamiento'),
(39, 'puebladelrio@gmail.com', 'scrypt:32768:8:1$EaZOLld0Kc9TC2b5$a8dd724c4a549eddf28edefec060824ea67e3be8ed14a1040d3dfbcc434075fc31a42dbbe853a906322a4d97fc1c03566ff2ecbb67736cacab9a6a1c05d23e53', 'ayuntamiento'),
(40, 'chiclana@gmail.com', 'scrypt:32768:8:1$vevvQBGOifZzqoPW$21119820056ce2284fc38c60ba9a8f93e1042c015bbf76594c9d7d6d2c3ee47394784f6e261b579ae0c63f137b1cbcb483bfb6f1614b97a3718af164d16275e6', 'ayuntamiento'),
(41, 'pirotecniavirgennieves@gmail.com', 'scrypt:32768:8:1$zK98cADQbecYP40h$11ea62f397a7de6654fa95329b7d4ef3bae8e51411dc3792fb07ae6d6956141a45d4bc8e46cff61180baed0bd91b147b201f02eb300be13e6a59065ac6a6865f', 'publicitado'),
(42, 'djkevin@gmail.com', 'scrypt:32768:8:1$2esheKUy3Cf7wVFi$69cd4ef5ec63f2b0b6d389d75cafd77e36aee6c340c18d186ca7c17c61ef713acb3596f9f83e894b34a100e8feae3e8a65f41b338ab99e09c3e82196c93bbc6e', 'publicitado'),
(43, 'admin2@gmail.com', 'scrypt:32768:8:1$3ImRu7wtw0K5Lk8X$690caad40342108febd4edbc230fc17f31cb7e37e8bce1b5b31e1d389cb26058c5bf4fa6bdcfa3f24bb3bba012a9644f4edb8f43f40a047500f6816340442a32', 'admin'),
(44, 'alcalaguadaira@gmail.com', 'scrypt:32768:8:1$1adc5dh77fNbmTei$08dff052e18eb86920f5061ef9b215c122d4185f12f158095e4816cd361e2ec8c7c96ae1cb81171a555ca47fef2238c0d278378e55b174fc6127a1ef969d4356', 'ayuntamiento'),
(45, 'articulospaco@gmail.com', 'scrypt:32768:8:1$VAqqETIVYVmMWtGK$195c55d8db429ab5f10b2148339462a36ccea42aaf211397dfa3516227b3b71c015b8bf130fc645e87563586b22a5cfd20af1626690f7e29b7da381bd29f1212', 'feriante'),
(46, 'atraccionesmillan@gmail.com', 'scrypt:32768:8:1$SCTlp5bqfe57llBi$24453afeeb9f9c2851c6571b6b07789b94a306f7a0ed4b22a0a95e1863115260e3813f167c2f573c8d63f1a7f5d6cbc0379be6918e7f75232cc5eed0dd049fc9', 'feriante');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `ayuntamiento`
--
ALTER TABLE `ayuntamiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `feriante`
--
ALTER TABLE `feriante`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `fiesta`
--
ALTER TABLE `fiesta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idAyun` (`idAyun`);

--
-- Indices de la tabla `fiesta_parcela`
--
ALTER TABLE `fiesta_parcela`
  ADD PRIMARY KEY (`fiesta_id`,`parcela_id`),
  ADD KEY `parcela_id` (`parcela_id`);

--
-- Indices de la tabla `parcela`
--
ALTER TABLE `parcela`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idAyun` (`idAyun`);

--
-- Indices de la tabla `publicidad`
--
ALTER TABLE `publicidad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD KEY `idPublicitado` (`idPublicitado`);

--
-- Indices de la tabla `publicitado`
--
ALTER TABLE `publicitado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `solicitud`
--
ALTER TABLE `solicitud`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idFeriante` (`idFeriante`),
  ADD KEY `idParcela` (`idParcela`),
  ADD KEY `idFiesta` (`idFiesta`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `ayuntamiento`
--
ALTER TABLE `ayuntamiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `feriante`
--
ALTER TABLE `feriante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `fiesta`
--
ALTER TABLE `fiesta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `parcela`
--
ALTER TABLE `parcela`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `publicidad`
--
ALTER TABLE `publicidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `publicitado`
--
ALTER TABLE `publicitado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `solicitud`
--
ALTER TABLE `solicitud`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `ayuntamiento`
--
ALTER TABLE `ayuntamiento`
  ADD CONSTRAINT `ayuntamiento_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `feriante`
--
ALTER TABLE `feriante`
  ADD CONSTRAINT `feriante_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `fiesta`
--
ALTER TABLE `fiesta`
  ADD CONSTRAINT `fiesta_ibfk_1` FOREIGN KEY (`idAyun`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `fiesta_parcela`
--
ALTER TABLE `fiesta_parcela`
  ADD CONSTRAINT `fiesta_parcela_ibfk_1` FOREIGN KEY (`fiesta_id`) REFERENCES `fiesta` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fiesta_parcela_ibfk_2` FOREIGN KEY (`parcela_id`) REFERENCES `parcela` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `parcela`
--
ALTER TABLE `parcela`
  ADD CONSTRAINT `parcela_ibfk_1` FOREIGN KEY (`idAyun`) REFERENCES `ayuntamiento` (`usuario_id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `publicidad`
--
ALTER TABLE `publicidad`
  ADD CONSTRAINT `publicidad_ibfk_1` FOREIGN KEY (`idPublicitado`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `publicitado`
--
ALTER TABLE `publicitado`
  ADD CONSTRAINT `publicitado_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `solicitud`
--
ALTER TABLE `solicitud`
  ADD CONSTRAINT `solicitud_ibfk_1` FOREIGN KEY (`idFeriante`) REFERENCES `feriante` (`usuario_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `solicitud_ibfk_2` FOREIGN KEY (`idParcela`) REFERENCES `parcela` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `solicitud_ibfk_3` FOREIGN KEY (`idFiesta`) REFERENCES `fiesta` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
