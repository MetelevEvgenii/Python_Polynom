import unittest

#@total_ordering для перегрузки другой половины сравнения

class Polynom(object):
    def __init__(self, mylist = []):
        self.coeffs = mylist

    def equalLength(self, other):
        while len(self.coeffs) != len(other.coeffs):
            if len(self.coeffs) < len(other.coeffs):
                self.coeffs.insert(0, 0)
            else:
                other.coeffs.insert(0, 0)
            pass

    def __str__(self):
        st = ""
        iterator = 0
        for i in self.coeffs:
            if i != 0:
                if st != "":
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
            else:
                iterator += 1
        return st
        pass

    def __eq__(self, other):
        return self.coeffs == other.coeffs

    def __gt__(self, other):
        num = 0
        for cof in self.coeffs:
            if cof > other.coeffs[num]:
                return True
            elif cof < other.coeffs[num]:
                return False
            else:
                num += 1
        return False

    def __ge__(self, other):
        num = 0
        for cof in self.coeffs:
            if cof > other.coeffs[num]:
                return True
            elif cof < other.coeffs[num]:
                return False
            else:
                num += 1
        return True

    def __add__(self, other):
        sumPol = Polynom
        sumList = []
        self.equalLength(other)
        if len(self.coeffs) == len(other.coeffs):
            for i, value in enumerate(self.coeffs, 0):
                sumList.append(self.coeffs[i] + other.coeffs[i])
        return sumPol(sumList)

    def __sub__(self, other):
        sumPol = Polynom
        sumList = []
        self.equalLength(other)
        if len(self.coeffs) == len(other.coeffs):
            for i, value in enumerate(self.coeffs, 0):
                sumList.append(self.coeffs[i] - other.coeffs[i])
        return sumPol(sumList)

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

    def testStrOutWithOneOnStart(self):
            list1 = [1, 7, 1, 3, 5, 10]
            pol = Polynom(list1)
            self.assertEqual("x^5+7x^4+x^3+3x^2+5x+10", pol.__str__())

    def testStrOutWithOneOnStartAndEnd(self):
        list1 = [1, 7, 1, 3, 5, 1]
        pol = Polynom(list1)
        self.assertEqual("x^5+7x^4+x^3+3x^2+5x+1", pol.__str__())

    def testStrOutWithMines(self):
        list1 = [1, -7, 1, -3, 5, -10]
        pol = Polynom(list1)
        self.assertEqual("x^5-7x^4+x^3-3x^2+5x-10", pol.__str__())

    def testStrOutWithMinesOnOneInStartAndEnd(self):
        list1 = [-1, -1, -2, -3, -5, -1]
        pol = Polynom(list1)
        self.assertEqual("-x^5-x^4-2x^3-3x^2-5x-1", pol.__str__())

    def testStrOutOnes(self):
        list1 = [1, 1, 1, 1, 1, 1]
        pol = Polynom(list1)
        self.assertEqual("x^5+x^4+x^3+x^2+x+1", pol.__str__())

    def testStrOutMinusOnes(self):
        list1 = [-1, -1, -1, -1, -1, -1]
        pol = Polynom(list1)
        self.assertEqual("-x^5-x^4-x^3-x^2-x-1", pol.__str__())

    def testStrOutWithZeroInMiddle(self):
            list1 = [3, 2, 0, 0, 0, 4]
            pol = Polynom(list1)
            self.assertEqual("3x^5+2x^4+4", pol.__str__())

    def testStrOutWithZeroInBegin(self):
            list1 = [0, 0, -1]
            pol = Polynom(list1)
            self.assertEqual("-1", pol.__str__())

    def testStrOutWithZeroInBegin(self):
        list1 = [0, 0, 1]
        pol = Polynom(list1)
        self.assertEqual("1", pol.__str__())

    def testStrOutWithZeroInBegin(self):
            list1 = [0, 5, -1]
            pol = Polynom(list1)
            self.assertEqual("5x-1", pol.__str__())

    def testStrOutWithZeroInBeginAndEnd(self):
        list1 = [0, 5, 0]
        pol = Polynom(list1)
        self.assertEqual("5x", pol.__str__())

    def testComparisonEquality(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 == pol2)

    def testComparisonNotEquality(self):
        list1 = [3, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertFalse(pol1 == pol2)

    def testComparisonMore(self):
        list1 = [3, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 > pol2)

    def testComparisonMore2(self):
        list1 = [1, 2, 3]
        list2 = [3, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertFalse(pol1 > pol2)

    def testComparisonMore3(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertFalse(pol1 > pol2)

    def testComparisonMore4(self):
        list1 = [1, 3, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 > pol2)

    def testComparisonMore5(self):
        list1 = [1, 2, 4]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 > pol2)

    def testComparisonMoreZeros(self):
        list1 = [1, 2, 3]
        list2 = [1, 0, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 > pol2)

    def testComparisonLess(self):
        list1 = [1, 3, 3]
        list2 = [2, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 < pol2)

    def testComparisonMoreOrEq(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 >= pol2)

    def testComparisonMoreOrEq2(self):
        list1 = [1, 3, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 >= pol2)

    def testComparisonMoreOrEq3(self):
        list1 = [4, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 >= pol2)

    def testComparisonMoreOrEq(self):
        list1 = [1, 0, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertFalse(pol1 >= pol2)

    def testComparisonMoreOrEq2(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 <= pol2)

    def testComparisonUnequal(self):
        list1 = [1, 3, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertTrue(pol1 != pol2)

    def testComparisonUnequal(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        self.assertFalse(pol1 != pol2)

    def testSum(self):
        list1 = [5, 2, 4]
        list2 = [3, 2, 1]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        pol3 = pol1 + pol2
        self.assertEqual(pol3.coeffs, [8, 4, 5])

    def testSum2(self):
        list1 = [12, 4, 5, 2, 4]
        list2 = [2, 1]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        pol3 = pol1 + pol2
        self.assertEqual(pol3.coeffs, [12, 4, 5, 4, 5])

    def testSum3(self):
        list1 = [12, -4, 5, -2, 4]
        list2 = [-3, 2, 1]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        pol3 = pol1 + pol2
        self.assertEqual(pol3.coeffs, [12, -4, 2, 0, 5])

    def testSum4(self):
        list1 = [-4, 5, -2, 4]
        list2 = [0, 5, -3, 2, 1]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        pol3 = pol1 + pol2
        self.assertEqual(pol3.coeffs, [0, 1, 2, 0, 5])

    def testSubtraction(self):
        list1 = [-4, 5, -2, 4]
        list2 = [0, 5, -3, 2, 1]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        pol3 = pol1 - pol2
        self.assertEqual(pol3.coeffs, [0, -9, 8, -4, 3])

    def testConstMult(self):
        list1 = [-2, 4]
        list2 = [-3, 2, 1]
        pol1 = Polynom(list1)
        pol2 = Polynom(list2)
        pol3 = pol1 - pol2
        self.assertEqual(pol3.coeffs, [0, -9, 8, -4, 3])


pass


if __name__ == '__main__':
    unittest.main()
