import unittest


class Polynom(object):
    def __init__(self, mylist = []):
        self.coeffs = mylist

    def __str__(self):
        st = ""
        iterator = 0
        for i in self.coeffs:
            if i != 0:
                if iterator != 0:
                    if i > 0:
                        st += "+"
                if i == -1:
                    if iterator == len(self.coeffs)-1:
                        st += str(i)
                        break
                    st += "-"
                elif i != 1 or iterator == len(self.coeffs)-1:
                    st += str(i)

                degree = len(self.coeffs) - iterator - 1
                if degree > 1:
                    st += "x^" + str(degree)
                elif degree == 1:
                    st += "x"
                elif degree == 0:
                    st += ""
                iterator += 1
        return st
        pass


class TestPolynom(unittest.TestCase):

    def testInit(self):
        list1 = [1, 1, 1]
        pol = Polynom(list1)
        self.assertEqual(list1, pol.coeffs)

    def testStrOutWithoutOne(self):
        list1 = [3, 2, 5]
        pol = Polynom(list1)
        self.assertEqual("3x^2+2x+5", pol.__str__())

    def testStrOutWIthOneOnEnd(self):
        list1 = [3, 2, 1]
        pol = Polynom(list1)
        self.assertEqual("3x^2+2x+1", pol.__str__())

    def testStrOutWithOneToX(self):
            list1 = [1, 7, 1, 3, 5, 10]
            pol = Polynom(list1)
            self.assertEqual("x^5+7x^4+x^3+3x^2+5x+10", pol.__str__())

    def testStrOutWithMines(self):
        list1 = [1, -7, 1, -3, 5, -10]
        pol = Polynom(list1)
        self.assertEqual("x^5-7x^4+x^3-3x^2+5x-10", pol.__str__())

    def testStrOutWithMines2(self):
        list1 = [-1, -1, -2, -3, -5, -1]
        pol = Polynom(list1)
        self.assertEqual("-x^5-x^4-2x^3-3x^2-5x-1", pol.__str__())

    def testStrOutWithMines3(self):
        list1 = [1, 1, 1, 1, 1, 1]
        pol = Polynom(list1)
        self.assertEqual("x^5+x^4+x^3+x^2+x+1", pol.__str__())

    def testStrOutWithMines3(self):
        list1 = [-1, -1, -1, -1, -1, -1]
        pol = Polynom(list1)
        self.assertEqual("-x^5-x^4-x^3-x^2-x-1", pol.__str__())

pass


if __name__ == '__main__':
    unittest.main()
