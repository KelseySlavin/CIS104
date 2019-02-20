import unittest
import calculator

class Tests(unittest.TestCase):

    def testadd(self):
        self.assertequal (calculator.add (3, 10), 13)
        self.assertequal (calculator.add (500, 2), 502)
        self.assertequal (calculator.add (-20, 5), 20)

    def testsub(self):
        self.assertequal (calculator.sub(6, 3), 3)
        self.assertequal (calculator.sub(50, 5), 45)
        self.assertequal (calculator.sub(6, -3), 9)

    def testmulti(self):
        self.assertequal (calulator.multi(2, 6), 12)
        self.assertequal (calulator.multi(20, 2), 40)
        self.assertequal (calulator.multi(100, 5), 500)

    def testdivide(self):
        
        

        

if __name__ == '__main__':
    unittest.main()