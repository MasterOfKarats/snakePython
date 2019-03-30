import unittest
from lecture import FirstObject

class UnitTesting(unittest.TestCase):

    def test_compute(self):
        result = API.computeShippingCost(30)
        self.assertEqual(result , "remaining: 50")

    def test_compute2(self):
        result = FirstObject.computeShippingCost(0)
        self.assertEqual(result , 5)

    def test_compute3(self):
        result = FirstObject.computeShippingCost(-23)
        self.assertEqual(result , 5)

    def test_compute4(self):
        result = FirstObject.computeShippingCost(100)
        self.assertEqual(result , 22.5)


if __name__ == '__main__':
    unittest.main()
