class GestureTemplate:
    def __init__(self, name, path):
        self.Name = name
        self.Path = path

class Point2D:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

class Path2D:
    def __init__(self, points:list):
        self.Points = points
    pass


class TuioGestures:
    templates = [
        GestureTemplate(
            "Delete",
            [
                Point2D(123, 129),
                Point2D(123, 131),
                Point2D(124, 133),
                Point2D(125, 136),
                Point2D(127, 140),
                Point2D(129, 142),
                Point2D(133, 148),
                Point2D(137, 154),
                Point2D(143, 158),
                Point2D(145, 161),
                Point2D(148, 164),
                Point2D(153, 170),
                Point2D(158, 176),
                Point2D(160, 178),
                Point2D(164, 183),
                Point2D(168, 188),
                Point2D(171, 191),
                Point2D(175, 196),
                Point2D(178, 200),
                Point2D(180, 202),
                Point2D(181, 205),
                Point2D(184, 208),
                Point2D(186, 210),
                Point2D(187, 213),
                Point2D(188, 215),
                Point2D(186, 212),
                Point2D(183, 211),
                Point2D(177, 208),
                Point2D(169, 206),
                Point2D(162, 205),
                Point2D(154, 207),
                Point2D(145, 209),
                Point2D(137, 210),
                Point2D(129, 214),
                Point2D(122, 217),
                Point2D(118, 218),
                Point2D(111, 221),
                Point2D(109, 222),
                Point2D(110, 219),
                Point2D(112, 217),
                Point2D(118, 209),
                Point2D(120, 207),
                Point2D(128, 196),
                Point2D(135, 187),
                Point2D(138, 183),
                Point2D(148, 167),
                Point2D(157, 153),
                Point2D(163, 145),
                Point2D(165, 142),
                Point2D(172, 133),
                Point2D(177, 127),
                Point2D(179, 127),
                Point2D(180, 125),
            ],
        ),
        GestureTemplate(
            "Arrow",
            [
                Point2D(68, 222),
                Point2D(70, 220),
                Point2D(73, 218),
                Point2D(75, 217),
                Point2D(77, 215),
                Point2D(80, 213),
                Point2D(82, 212),
                Point2D(84, 210),
                Point2D(87, 209),
                Point2D(89, 208),
                Point2D(92, 206),
                Point2D(95, 204),
                Point2D(101, 201),
                Point2D(106, 198),
                Point2D(112, 194),
                Point2D(118, 191),
                Point2D(124, 187),
                Point2D(127, 186),
                Point2D(132, 183),
                Point2D(138, 181),
                Point2D(141, 180),
                Point2D(146, 178),
                Point2D(154, 173),
                Point2D(159, 171),
                Point2D(161, 170),
                Point2D(166, 167),
                Point2D(168, 167),
                Point2D(171, 166),
                Point2D(174, 164),
                Point2D(177, 162),
                Point2D(180, 160),
                Point2D(182, 158),
                Point2D(183, 156),
                Point2D(181, 154),
                Point2D(178, 153),
                Point2D(171, 153),
                Point2D(164, 153),
                Point2D(160, 153),
                Point2D(150, 154),
                Point2D(147, 155),
                Point2D(141, 157),
                Point2D(137, 158),
                Point2D(135, 158),
                Point2D(137, 158),
                Point2D(140, 157),
                Point2D(143, 156),
                Point2D(151, 154),
                Point2D(160, 152),
                Point2D(170, 149),
                Point2D(179, 147),
                Point2D(185, 145),
                Point2D(192, 144),
                Point2D(196, 144),
                Point2D(198, 144),
                Point2D(200, 144),
                Point2D(201, 147),
                Point2D(199, 149),
                Point2D(194, 157),
                Point2D(191, 160),
                Point2D(186, 167),
                Point2D(180, 176),
                Point2D(177, 179),
                Point2D(171, 187),
                Point2D(169, 189),
                Point2D(165, 194),
                Point2D(164, 196),
            ],
        ),
        GestureTemplate(
            "Caret",
            [
                Point2D(79, 245),
                Point2D(79, 242),
                Point2D(79, 239),
                Point2D(80, 237),
                Point2D(80, 234),
                Point2D(81, 232),
                Point2D(82, 230),
                Point2D(84, 224),
                Point2D(86, 220),
                Point2D(86, 218),
                Point2D(87, 216),
                Point2D(88, 213),
                Point2D(90, 207),
                Point2D(91, 202),
                Point2D(92, 200),
                Point2D(93, 194),
                Point2D(94, 192),
                Point2D(96, 189),
                Point2D(97, 186),
                Point2D(100, 179),
                Point2D(102, 173),
                Point2D(105, 165),
                Point2D(107, 160),
                Point2D(109, 158),
                Point2D(112, 151),
                Point2D(115, 144),
                Point2D(117, 139),
                Point2D(119, 136),
                Point2D(119, 134),
                Point2D(120, 132),
                Point2D(121, 129),
                Point2D(122, 127),
                Point2D(124, 125),
                Point2D(126, 124),
                Point2D(129, 125),
                Point2D(131, 127),
                Point2D(132, 130),
                Point2D(136, 139),
                Point2D(141, 154),
                Point2D(145, 166),
                Point2D(151, 182),
                Point2D(156, 193),
                Point2D(157, 196),
                Point2D(161, 209),
                Point2D(162, 211),
                Point2D(167, 223),
                Point2D(169, 229),
                Point2D(170, 231),
                Point2D(173, 237),
                Point2D(176, 242),
                Point2D(177, 244),
                Point2D(179, 250),
                Point2D(181, 255),
                Point2D(182, 257),
            ],
        ),
        GestureTemplate(
            "Check",
            [
                Point2D(91, 185),
                Point2D(93, 185),
                Point2D(95, 185),
                Point2D(97, 185),
                Point2D(100, 188),
                Point2D(102, 189),
                Point2D(104, 190),
                Point2D(106, 193),
                Point2D(108, 195),
                Point2D(110, 198),
                Point2D(112, 201),
                Point2D(114, 204),
                Point2D(115, 207),
                Point2D(117, 210),
                Point2D(118, 212),
                Point2D(120, 214),
                Point2D(121, 217),
                Point2D(122, 219),
                Point2D(123, 222),
                Point2D(124, 224),
                Point2D(126, 226),
                Point2D(127, 229),
                Point2D(129, 231),
                Point2D(130, 233),
                Point2D(129, 231),
                Point2D(129, 228),
                Point2D(129, 226),
                Point2D(129, 224),
                Point2D(129, 221),
                Point2D(129, 218),
                Point2D(129, 212),
                Point2D(129, 208),
                Point2D(130, 198),
                Point2D(132, 189),
                Point2D(134, 182),
                Point2D(137, 173),
                Point2D(143, 164),
                Point2D(147, 157),
                Point2D(151, 151),
                Point2D(155, 144),
                Point2D(161, 137),
                Point2D(165, 131),
                Point2D(171, 122),
                Point2D(174, 118),
                Point2D(176, 114),
                Point2D(177, 112),
                Point2D(177, 114),
                Point2D(175, 116),
                Point2D(173, 118),
            ],
        ),
        GestureTemplate(
            "Circle",
            [
                Point2D(127, 141),
                Point2D(124, 140),
                Point2D(120, 139),
                Point2D(118, 139),
                Point2D(116, 139),
                Point2D(111, 140),
                Point2D(109, 141),
                Point2D(104, 144),
                Point2D(100, 147),
                Point2D(96, 152),
                Point2D(93, 157),
                Point2D(90, 163),
                Point2D(87, 169),
                Point2D(85, 175),
                Point2D(83, 181),
                Point2D(82, 190),
                Point2D(82, 195),
                Point2D(83, 200),
                Point2D(84, 205),
                Point2D(88, 213),
                Point2D(91, 216),
                Point2D(96, 219),
                Point2D(103, 222),
                Point2D(108, 224),
                Point2D(111, 224),
                Point2D(120, 224),
                Point2D(133, 223),
                Point2D(142, 222),
                Point2D(152, 218),
                Point2D(160, 214),
                Point2D(167, 210),
                Point2D(173, 204),
                Point2D(178, 198),
                Point2D(179, 196),
                Point2D(182, 188),
                Point2D(182, 177),
                Point2D(178, 167),
                Point2D(170, 150),
                Point2D(163, 138),
                Point2D(152, 130),
                Point2D(143, 129),
                Point2D(140, 131),
                Point2D(129, 136),
                Point2D(126, 139),
            ],
        ),
        GestureTemplate(
            "Delete",
            [
                Point2D(123, 129),
                Point2D(123, 131),
                Point2D(124, 133),
                Point2D(125, 136),
                Point2D(127, 140),
                Point2D(129, 142),
                Point2D(133, 148),
                Point2D(137, 154),
                Point2D(143, 158),
                Point2D(145, 161),
                Point2D(148, 164),
                Point2D(153, 170),
                Point2D(158, 176),
                Point2D(160, 178),
                Point2D(164, 183),
                Point2D(168, 188),
                Point2D(171, 191),
                Point2D(175, 196),
                Point2D(178, 200),
                Point2D(180, 202),
                Point2D(181, 205),
                Point2D(184, 208),
                Point2D(186, 210),
                Point2D(187, 213),
                Point2D(188, 215),
                Point2D(186, 212),
                Point2D(183, 211),
                Point2D(177, 208),
                Point2D(169, 206),
                Point2D(162, 205),
                Point2D(154, 207),
                Point2D(145, 209),
                Point2D(137, 210),
                Point2D(129, 214),
                Point2D(122, 217),
                Point2D(118, 218),
                Point2D(111, 221),
                Point2D(109, 222),
                Point2D(110, 219),
                Point2D(112, 217),
                Point2D(118, 209),
                Point2D(120, 207),
                Point2D(128, 196),
                Point2D(135, 187),
                Point2D(138, 183),
                Point2D(148, 167),
                Point2D(157, 153),
                Point2D(163, 145),
                Point2D(165, 142),
                Point2D(172, 133),
                Point2D(177, 127),
                Point2D(179, 127),
                Point2D(180, 125),
            ],
        ),
        
        GestureTemplate(
            "LeftCurlyBrace",
            [
                Point2D(150, 116),
                Point2D(147, 117),
                Point2D(145, 116),
                Point2D(142, 116),
                Point2D(139, 117),
                Point2D(136, 117),
                Point2D(133, 118),
                Point2D(129, 121),
                Point2D(126, 122),
                Point2D(123, 123),
                Point2D(120, 125),
                Point2D(118, 127),
                Point2D(115, 128),
                Point2D(113, 129),
                Point2D(112, 131),
                Point2D(113, 134),
                Point2D(115, 134),
                Point2D(117, 135),
                Point2D(120, 135),
                Point2D(123, 137),
                Point2D(126, 138),
                Point2D(129, 140),
                Point2D(135, 143),
                Point2D(137, 144),
                Point2D(139, 147),
                Point2D(141, 149),
                Point2D(140, 152),
                Point2D(139, 155),
                Point2D(134, 159),
                Point2D(131, 161),
                Point2D(124, 166),
                Point2D(121, 166),
                Point2D(117, 166),
                Point2D(114, 167),
                Point2D(112, 166),
                Point2D(114, 164),
                Point2D(116, 163),
                Point2D(118, 163),
                Point2D(120, 162),
                Point2D(122, 163),
                Point2D(125, 164),
                Point2D(127, 165),
                Point2D(129, 166),
                Point2D(130, 168),
                Point2D(129, 171),
                Point2D(127, 175),
                Point2D(125, 179),
                Point2D(123, 184),
                Point2D(121, 190),
                Point2D(120, 194),
                Point2D(119, 199),
                Point2D(120, 202),
                Point2D(123, 207),
                Point2D(127, 211),
                Point2D(133, 215),
                Point2D(142, 219),
                Point2D(148, 220),
                Point2D(151, 221),
            ],
        ),
        GestureTemplate(
            "LeftSquareBracket",
            [
                Point2D(140, 124),
                Point2D(138, 123),
                Point2D(135, 122),
                Point2D(133, 123),
                Point2D(130, 123),
                Point2D(128, 124),
                Point2D(125, 125),
                Point2D(122, 124),
                Point2D(120, 124),
                Point2D(118, 124),
                Point2D(116, 125),
                Point2D(113, 125),
                Point2D(111, 125),
                Point2D(108, 124),
                Point2D(106, 125),
                Point2D(104, 125),
                Point2D(102, 124),
                Point2D(100, 123),
                Point2D(98, 123),
                Point2D(95, 124),
                Point2D(93, 123),
                Point2D(90, 124),
                Point2D(88, 124),
                Point2D(85, 125),
                Point2D(83, 126),
                Point2D(81, 127),
                Point2D(81, 129),
                Point2D(82, 131),
                Point2D(82, 134),
                Point2D(83, 138),
                Point2D(84, 141),
                Point2D(84, 144),
                Point2D(85, 148),
                Point2D(85, 151),
                Point2D(86, 156),
                Point2D(86, 160),
                Point2D(86, 164),
                Point2D(86, 168),
                Point2D(87, 171),
                Point2D(87, 175),
                Point2D(87, 179),
                Point2D(87, 182),
                Point2D(87, 186),
                Point2D(88, 188),
                Point2D(88, 195),
                Point2D(88, 198),
                Point2D(88, 201),
                Point2D(88, 207),
                Point2D(89, 211),
                Point2D(89, 213),
                Point2D(89, 217),
                Point2D(89, 222),
                Point2D(88, 225),
                Point2D(88, 229),
                Point2D(88, 231),
                Point2D(88, 233),
                Point2D(88, 235),
                Point2D(89, 237),
                Point2D(89, 240),
                Point2D(89, 242),
                Point2D(91, 241),
                Point2D(94, 241),
                Point2D(96, 240),
                Point2D(98, 239),
                Point2D(105, 240),
                Point2D(109, 240),
                Point2D(113, 239),
                Point2D(116, 240),
                Point2D(121, 239),
                Point2D(130, 240),
                Point2D(136, 237),
                Point2D(139, 237),
                Point2D(144, 238),
                Point2D(151, 237),
                Point2D(157, 236),
                Point2D(159, 237),
            ],
        ),
        GestureTemplate(
            "Pigtail",
            [
                Point2D(81, 219),
                Point2D(84, 218),
                Point2D(86, 220),
                Point2D(88, 220),
                Point2D(90, 220),
                Point2D(92, 219),
                Point2D(95, 220),
                Point2D(97, 219),
                Point2D(99, 220),
                Point2D(102, 218),
                Point2D(105, 217),
                Point2D(107, 216),
                Point2D(110, 216),
                Point2D(113, 214),
                Point2D(116, 212),
                Point2D(118, 210),
                Point2D(121, 208),
                Point2D(124, 205),
                Point2D(126, 202),
                Point2D(129, 199),
                Point2D(132, 196),
                Point2D(136, 191),
                Point2D(139, 187),
                Point2D(142, 182),
                Point2D(144, 179),
                Point2D(146, 174),
                Point2D(148, 170),
                Point2D(149, 168),
                Point2D(151, 162),
                Point2D(152, 160),
                Point2D(152, 157),
                Point2D(152, 155),
                Point2D(152, 151),
                Point2D(152, 149),
                Point2D(152, 146),
                Point2D(149, 142),
                Point2D(148, 139),
                Point2D(145, 137),
                Point2D(141, 135),
                Point2D(139, 135),
                Point2D(134, 136),
                Point2D(130, 140),
                Point2D(128, 142),
                Point2D(126, 145),
                Point2D(122, 150),
                Point2D(119, 158),
                Point2D(117, 163),
                Point2D(115, 170),
                Point2D(114, 175),
                Point2D(117, 184),
                Point2D(120, 190),
                Point2D(125, 199),
                Point2D(129, 203),
                Point2D(133, 208),
                Point2D(138, 213),
                Point2D(145, 215),
                Point2D(155, 218),
                Point2D(164, 219),
                Point2D(166, 219),
                Point2D(177, 219),
                Point2D(182, 218),
                Point2D(192, 216),
                Point2D(196, 213),
                Point2D(199, 212),
                Point2D(201, 211),
            ],
        ),
        GestureTemplate(
            "Rectangle",
            [
                Point2D(78, 149),
                Point2D(78, 153),
                Point2D(78, 157),
                Point2D(78, 160),
                Point2D(79, 162),
                Point2D(79, 164),
                Point2D(79, 167),
                Point2D(79, 169),
                Point2D(79, 173),
                Point2D(79, 178),
                Point2D(79, 183),
                Point2D(80, 189),
                Point2D(80, 193),
                Point2D(80, 198),
                Point2D(80, 202),
                Point2D(81, 208),
                Point2D(81, 210),
                Point2D(81, 216),
                Point2D(82, 222),
                Point2D(82, 224),
                Point2D(82, 227),
                Point2D(83, 229),
                Point2D(83, 231),
                Point2D(85, 230),
                Point2D(88, 232),
                Point2D(90, 233),
                Point2D(92, 232),
                Point2D(94, 233),
                Point2D(99, 232),
                Point2D(102, 233),
                Point2D(106, 233),
                Point2D(109, 234),
                Point2D(117, 235),
                Point2D(123, 236),
                Point2D(126, 236),
                Point2D(135, 237),
                Point2D(142, 238),
                Point2D(145, 238),
                Point2D(152, 238),
                Point2D(154, 239),
                Point2D(165, 238),
                Point2D(174, 237),
                Point2D(179, 236),
                Point2D(186, 235),
                Point2D(191, 235),
                Point2D(195, 233),
                Point2D(197, 233),
                Point2D(200, 233),
                Point2D(201, 235),
                Point2D(201, 233),
                Point2D(199, 231),
                Point2D(198, 226),
                Point2D(198, 220),
                Point2D(196, 207),
                Point2D(195, 195),
                Point2D(195, 181),
                Point2D(195, 173),
                Point2D(195, 163),
                Point2D(194, 155),
                Point2D(192, 145),
                Point2D(192, 143),
                Point2D(192, 138),
                Point2D(191, 135),
                Point2D(191, 133),
                Point2D(191, 130),
                Point2D(190, 128),
                Point2D(188, 129),
                Point2D(186, 129),
                Point2D(181, 132),
                Point2D(173, 131),
                Point2D(162, 131),
                Point2D(151, 132),
                Point2D(149, 132),
                Point2D(138, 132),
                Point2D(136, 132),
                Point2D(122, 131),
                Point2D(120, 131),
                Point2D(109, 130),
                Point2D(107, 130),
                Point2D(90, 132),
                Point2D(81, 133),
                Point2D(76, 133),
            ],
        ),
        GestureTemplate(
            "RightSquareBracket",
            [
                Point2D(112, 138),
                Point2D(112, 136),
                Point2D(115, 136),
                Point2D(118, 137),
                Point2D(120, 136),
                Point2D(123, 136),
                Point2D(125, 136),
                Point2D(128, 136),
                Point2D(131, 136),
                Point2D(134, 135),
                Point2D(137, 135),
                Point2D(140, 134),
                Point2D(143, 133),
                Point2D(145, 132),
                Point2D(147, 132),
                Point2D(149, 132),
                Point2D(152, 132),
                Point2D(153, 134),
                Point2D(154, 137),
                Point2D(155, 141),
                Point2D(156, 144),
                Point2D(157, 152),
                Point2D(158, 161),
                Point2D(160, 170),
                Point2D(162, 182),
                Point2D(164, 192),
                Point2D(166, 200),
                Point2D(167, 209),
                Point2D(168, 214),
                Point2D(168, 216),
                Point2D(169, 221),
                Point2D(169, 223),
                Point2D(169, 228),
                Point2D(169, 231),
                Point2D(166, 233),
                Point2D(164, 234),
                Point2D(161, 235),
                Point2D(155, 236),
                Point2D(147, 235),
                Point2D(140, 233),
                Point2D(131, 233),
                Point2D(124, 233),
                Point2D(117, 235),
                Point2D(114, 238),
                Point2D(112, 238),
            ],
        ),
        GestureTemplate(
            "RightCurlyBrace",
            [
                Point2D(117, 132),
                Point2D(115, 132),
                Point2D(115, 129),
                Point2D(117, 129),
                Point2D(119, 128),
                Point2D(122, 127),
                Point2D(125, 127),
                Point2D(127, 127),
                Point2D(130, 127),
                Point2D(133, 129),
                Point2D(136, 129),
                Point2D(138, 130),
                Point2D(140, 131),
                Point2D(143, 134),
                Point2D(144, 136),
                Point2D(145, 139),
                Point2D(145, 142),
                Point2D(145, 145),
                Point2D(145, 147),
                Point2D(145, 149),
                Point2D(144, 152),
                Point2D(142, 157),
                Point2D(141, 160),
                Point2D(139, 163),
                Point2D(137, 166),
                Point2D(135, 167),
                Point2D(133, 169),
                Point2D(131, 172),
                Point2D(128, 173),
                Point2D(126, 176),
                Point2D(125, 178),
                Point2D(125, 180),
                Point2D(125, 182),
                Point2D(126, 184),
                Point2D(128, 187),
                Point2D(130, 187),
                Point2D(132, 188),
                Point2D(135, 189),
                Point2D(140, 189),
                Point2D(145, 189),
                Point2D(150, 187),
                Point2D(155, 186),
                Point2D(157, 185),
                Point2D(159, 184),
                Point2D(156, 185),
                Point2D(154, 185),
                Point2D(149, 185),
                Point2D(145, 187),
                Point2D(141, 188),
                Point2D(136, 191),
                Point2D(134, 191),
                Point2D(131, 192),
                Point2D(129, 193),
                Point2D(129, 195),
                Point2D(129, 197),
                Point2D(131, 200),
                Point2D(133, 202),
                Point2D(136, 206),
                Point2D(139, 211),
                Point2D(142, 215),
                Point2D(145, 220),
                Point2D(147, 225),
                Point2D(148, 231),
                Point2D(147, 239),
                Point2D(144, 244),
                Point2D(139, 248),
                Point2D(134, 250),
                Point2D(126, 253),
                Point2D(119, 253),
                Point2D(115, 253),
            ],
        ),
        GestureTemplate(
            "Star",
            [
                Point2D(75, 250),
                Point2D(75, 247),
                Point2D(77, 244),
                Point2D(78, 242),
                Point2D(79, 239),
                Point2D(80, 237),
                Point2D(82, 234),
                Point2D(82, 232),
                Point2D(84, 229),
                Point2D(85, 225),
                Point2D(87, 222),
                Point2D(88, 219),
                Point2D(89, 216),
                Point2D(91, 212),
                Point2D(92, 208),
                Point2D(94, 204),
                Point2D(95, 201),
                Point2D(96, 196),
                Point2D(97, 194),
                Point2D(98, 191),
                Point2D(100, 185),
                Point2D(102, 178),
                Point2D(104, 173),
                Point2D(104, 171),
                Point2D(105, 164),
                Point2D(106, 158),
                Point2D(107, 156),
                Point2D(107, 152),
                Point2D(108, 145),
                Point2D(109, 141),
                Point2D(110, 139),
                Point2D(112, 133),
                Point2D(113, 131),
                Point2D(116, 127),
                Point2D(117, 125),
                Point2D(119, 122),
                Point2D(121, 121),
                Point2D(123, 120),
                Point2D(125, 122),
                Point2D(125, 125),
                Point2D(127, 130),
                Point2D(128, 133),
                Point2D(131, 143),
                Point2D(136, 153),
                Point2D(140, 163),
                Point2D(144, 172),
                Point2D(145, 175),
                Point2D(151, 189),
                Point2D(156, 201),
                Point2D(161, 213),
                Point2D(166, 225),
                Point2D(169, 233),
                Point2D(171, 236),
                Point2D(174, 243),
                Point2D(177, 247),
                Point2D(178, 249),
                Point2D(179, 251),
                Point2D(180, 253),
                Point2D(180, 255),
                Point2D(179, 257),
                Point2D(177, 257),
                Point2D(174, 255),
                Point2D(169, 250),
                Point2D(164, 247),
                Point2D(160, 245),
                Point2D(149, 238),
                Point2D(138, 230),
                Point2D(127, 221),
                Point2D(124, 220),
                Point2D(112, 212),
                Point2D(110, 210),
                Point2D(96, 201),
                Point2D(84, 195),
                Point2D(74, 190),
                Point2D(64, 182),
                Point2D(55, 175),
                Point2D(51, 172),
                Point2D(49, 170),
                Point2D(51, 169),
                Point2D(56, 169),
                Point2D(66, 169),
                Point2D(78, 168),
                Point2D(92, 166),
                Point2D(107, 164),
                Point2D(123, 161),
                Point2D(140, 162),
                Point2D(156, 162),
                Point2D(171, 160),
                Point2D(173, 160),
                Point2D(186, 160),
                Point2D(195, 160),
                Point2D(198, 161),
                Point2D(203, 163),
                Point2D(208, 163),
                Point2D(206, 164),
                Point2D(200, 167),
                Point2D(187, 172),
                Point2D(174, 179),
                Point2D(172, 181),
                Point2D(153, 192),
                Point2D(137, 201),
                Point2D(123, 211),
                Point2D(112, 220),
                Point2D(99, 229),
                Point2D(90, 237),
                Point2D(80, 244),
                Point2D(73, 250),
                Point2D(69, 254),
                Point2D(69, 252),
            ],
        ),
        GestureTemplate(
            "Triangle",
            [
                Point2D(137, 139),
                Point2D(135, 141),
                Point2D(133, 144),
                Point2D(132, 146),
                Point2D(130, 149),
                Point2D(128, 151),
                Point2D(126, 155),
                Point2D(123, 160),
                Point2D(120, 166),
                Point2D(116, 171),
                Point2D(112, 177),
                Point2D(107, 183),
                Point2D(102, 188),
                Point2D(100, 191),
                Point2D(95, 195),
                Point2D(90, 199),
                Point2D(86, 203),
                Point2D(82, 206),
                Point2D(80, 209),
                Point2D(75, 213),
                Point2D(73, 213),
                Point2D(70, 216),
                Point2D(67, 219),
                Point2D(64, 221),
                Point2D(61, 223),
                Point2D(60, 225),
                Point2D(62, 226),
                Point2D(65, 225),
                Point2D(67, 226),
                Point2D(74, 226),
                Point2D(77, 227),
                Point2D(85, 229),
                Point2D(91, 230),
                Point2D(99, 231),
                Point2D(108, 232),
                Point2D(116, 233),
                Point2D(125, 233),
                Point2D(134, 234),
                Point2D(145, 233),
                Point2D(153, 232),
                Point2D(160, 233),
                Point2D(170, 234),
                Point2D(177, 235),
                Point2D(179, 236),
                Point2D(186, 237),
                Point2D(193, 238),
                Point2D(198, 239),
                Point2D(200, 237),
                Point2D(202, 239),
                Point2D(204, 238),
                Point2D(206, 234),
                Point2D(205, 230),
                Point2D(202, 222),
                Point2D(197, 216),
                Point2D(192, 207),
                Point2D(186, 198),
                Point2D(179, 189),
                Point2D(174, 183),
                Point2D(170, 178),
                Point2D(164, 171),
                Point2D(161, 168),
                Point2D(154, 160),
                Point2D(148, 155),
                Point2D(143, 150),
                Point2D(138, 148),
                Point2D(136, 148),
            ],
        ),
        GestureTemplate(
            "V",
            [
                Point2D(89, 164),
                Point2D(90, 162),
                Point2D(92, 162),
                Point2D(94, 164),
                Point2D(95, 166),
                Point2D(96, 169),
                Point2D(97, 171),
                Point2D(99, 175),
                Point2D(101, 178),
                Point2D(103, 182),
                Point2D(106, 189),
                Point2D(108, 194),
                Point2D(111, 199),
                Point2D(114, 204),
                Point2D(117, 209),
                Point2D(119, 214),
                Point2D(122, 218),
                Point2D(124, 222),
                Point2D(126, 225),
                Point2D(128, 228),
                Point2D(130, 229),
                Point2D(133, 233),
                Point2D(134, 236),
                Point2D(136, 239),
                Point2D(138, 240),
                Point2D(139, 242),
                Point2D(140, 244),
                Point2D(142, 242),
                Point2D(142, 240),
                Point2D(142, 237),
                Point2D(143, 235),
                Point2D(143, 233),
                Point2D(145, 229),
                Point2D(146, 226),
                Point2D(148, 217),
                Point2D(149, 208),
                Point2D(149, 205),
                Point2D(151, 196),
                Point2D(151, 193),
                Point2D(153, 182),
                Point2D(155, 172),
                Point2D(157, 165),
                Point2D(159, 160),
                Point2D(162, 155),
                Point2D(164, 150),
                Point2D(165, 148),
                Point2D(166, 146),
            ],
        ),
        GestureTemplate(
            "X",
            [
                Point2D(87, 142),
                Point2D(89, 145),
                Point2D(91, 148),
                Point2D(93, 151),
                Point2D(96, 155),
                Point2D(98, 157),
                Point2D(100, 160),
                Point2D(102, 162),
                Point2D(106, 167),
                Point2D(108, 169),
                Point2D(110, 171),
                Point2D(115, 177),
                Point2D(119, 183),
                Point2D(123, 189),
                Point2D(127, 193),
                Point2D(129, 196),
                Point2D(133, 200),
                Point2D(137, 206),
                Point2D(140, 209),
                Point2D(143, 212),
                Point2D(146, 215),
                Point2D(151, 220),
                Point2D(153, 222),
                Point2D(155, 223),
                Point2D(157, 225),
                Point2D(158, 223),
                Point2D(157, 218),
                Point2D(155, 211),
                Point2D(154, 208),
                Point2D(152, 200),
                Point2D(150, 189),
                Point2D(148, 179),
                Point2D(147, 170),
                Point2D(147, 158),
                Point2D(147, 148),
                Point2D(147, 141),
                Point2D(147, 136),
                Point2D(144, 135),
                Point2D(142, 137),
                Point2D(140, 139),
                Point2D(135, 145),
                Point2D(131, 152),
                Point2D(124, 163),
                Point2D(116, 177),
                Point2D(108, 191),
                Point2D(100, 206),
                Point2D(94, 217),
                Point2D(91, 222),
                Point2D(89, 225),
                Point2D(87, 226),
                Point2D(87, 224),
            ],
        ),
        # own
        GestureTemplate(
            "RightToLeftSlashDown",
            [
                Point2D(200, 170),
                Point2D(195, 171),
                Point2D(190, 172),
                Point2D(185, 173),
                Point2D(180, 174),
                Point2D(175, 175),
                Point2D(170, 176),
                Point2D(165, 177),
                Point2D(160, 178),
                Point2D(155, 179),
                Point2D(150, 180),
                Point2D(160, 181),
                Point2D(140, 182),
                Point2D(160, 183),
                Point2D(155, 184),
                Point2D(150, 185),
                Point2D(145, 186),
                Point2D(140, 187),
                Point2D(135, 188),
                Point2D(130, 189),
                Point2D(125, 190),
                Point2D(120, 191),
                Point2D(115, 192),
                Point2D(110, 193),
                Point2D(105, 194),
                Point2D(100, 195),
                Point2D(95, 196),
                Point2D(85, 197),
                Point2D(75, 198),
                Point2D(70, 199),
            ],
        ),
    ]