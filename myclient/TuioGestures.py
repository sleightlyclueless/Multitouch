from dollarpy import Template,Point,Recognizer

class TuioGestures:
    templates = [
        Template("Circle",[ 
            Point(127,141),Point(124,140),Point(120,139),Point(118,139),Point(116,139),Point(111,140),Point(109,141),Point(104,144),Point(100,147),Point(96,152),Point(93,157),Point(90,163),Point(87,169),Point(85,175),Point(83,181),Point(82,190),Point(82,195),Point(83,200),Point(84,205),Point(88,213),Point(91,216),Point(96,219),Point(103,222),Point(108,224),Point(111,224),Point(120,224),Point(133,223),Point(142,222),Point(152,218),Point(160,214),Point(167,210),Point(173,204),Point(178,198),Point(179,196),Point(182,188),Point(182,177),Point(178,167),Point(170,150),Point(163,138),Point(152,130),Point(143,129),Point(140,131),Point(129,136),Point(126,139)
            ]),
            Template("CheckMark",[
                Point(91,185),Point(93,185),Point(95,185),Point(97,185),Point(100,188),Point(102,189),Point(104,190),Point(106,193),Point(108,195),Point(110,198),Point(112,201),Point(114,204),Point(115,207),Point(117,210),Point(118,212),Point(120,214),Point(121,217),Point(122,219),Point(123,222),Point(124,224),Point(126,226),Point(127,229),Point(129,231),Point(130,233),Point(129,231),Point(129,228),Point(129,226),Point(129,224),Point(129,221),Point(129,218),Point(129,212),Point(129,208),Point(130,198),Point(132,189),Point(134,182),Point(137,173),Point(143,164),Point(147,157),Point(151,151),Point(155,144),Point(161,137),Point(165,131),Point(171,122),Point(174,118),Point(176,114),Point(177,112),Point(177,114),Point(175,116),Point(173,118)
            ]),
        ]
    recognizer = Recognizer(templates=templates)

    def recognize_gesture(self,points):
        gesture = self.recognizer.recognize(points)
        return gesture