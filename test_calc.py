import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(calc.calc(0.0, 5.0), 'F')

    def test_case_2(self):
        self.assertEqual(calc.calc(0.1, 5.0), 'F')

    def test_case_3(self):
        self.assertEqual(calc.calc(5.0, 5.0), 'D')

    def test_case_4(self):
        self.assertEqual(calc.calc(9.9, 5.0), 'B')

    def test_case_5(self):
        self.assertEqual(calc.calc(10.0, 5.0), 'B')

    def test_case_6(self):
        self.assertEqual(calc.calc(5.0, 0.0), 'F')

    def test_case_7(self):
        self.assertEqual(calc.calc(5.0, 0.1), 'F')

    def test_case_8(self):
        self.assertEqual(calc.calc(5.0, 9.9), 'B')

    def test_case_9(self):
        self.assertEqual(calc.calc(5.0, 10.0), 'B')

    def test_case_10(self):
        with self.assertRaises(ValueError):
            calc.calc(-1.0, -1.0)

    def test_case_11(self):
        with self.assertRaises(ValueError):
            calc.calc(-1.0, 5.0)

    def test_case_12(self):
        with self.assertRaises(ValueError):
            calc.calc(-1.0, 11.0)

    def test_case_13(self):
        with self.assertRaises(ValueError):
            calc.calc(5.0, -1.0)

    def test_case_14(self):
        self.assertEqual(calc.calc(5.0, 5.0), 'D')

    def test_case_15(self):
        with self.assertRaises(ValueError):
            calc.calc(5.0, 11.0)

    def test_case_16(self):
        with self.assertRaises(ValueError):
            calc.calc(11.0, -1.0)

    def test_case_17(self):
        with self.assertRaises(ValueError):
            calc.calc(11.0, 5.0)

    def test_case_18(self):
        with self.assertRaises(ValueError):
            calc.calc(11.0, 11.0)

if __name__ == '__main__':
    unittest.main()