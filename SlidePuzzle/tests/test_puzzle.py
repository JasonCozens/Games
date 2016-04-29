import unittest
import xmlrunner


class PuzzleTest(unittest.TestCase):

    def test_start(self):
        self.assertFalse("Failure test.")


def all_tests():
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(PuzzleTest),
    ])

if __name__ == '__main__':

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
