import unittest
from AndelaLoan import Loan


class Test(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(loan(10000, 12, 12), 11200)

    def test_it_does_not_take_more_than_100_year(self):
        self.assertEquals(loan(10000, 114, 12), "Invalid")


if __name__ == '__main__':
    unittest.main()
