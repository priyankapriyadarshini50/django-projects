import unittest
import test_module


class TestTestModule(unittest.TestCase):
    def test_sum(self):
        test_list1 = [1, 2, 3, 4]
        result = test_module.suml(test_list1)
        self.assertEqual(result, 10)

    def test_prod(self):
        test_list2 = [1, 2, 3, 4, 5]
        result = test_module.prodl(test_list2)
        self.assertEqual(result, 120)

if __name__ == '__main__':
    unittest.main()
