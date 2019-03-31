import unittest
import tests

class UnitTesting(unittest.TestCase):

    def test_compute(self):
        y_pos = 0
        x_pos = 12
        tests.moveSnake(12,12)
        self.assertEqual(y_pos , 0)
        self.assertEqual(x_pos , 12)

class UnitTesting2(unittest.TestCase):

    def test_compute(self):
        x=8
        tests.getX()
        self.assertEqual(x , 8)

class UnitTesting3(unittest.TestCase):

    def test_compute(self):
        y=5
        tests.getY()
        self.assertEqual(y , 5)

class UnitTesting4(unittest.TestCase):

    def check_Collision(self):
        x_pos=0
        y_pos=0
        self.assertEqual(y_pos , 15)
        self.assertEqual(x_pos , 25)


if __name__ == '__main__':
    unittest.main()


