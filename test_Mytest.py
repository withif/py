import Calc


class TestCalc:
    def testAdd1(self):
        a = 6
        b = 5
        c = 11
        calc = Calc()
        s = calc.add(a,b)
        assert s == c