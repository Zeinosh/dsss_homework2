import unittest
from math_quiz import function_random_min_max, function_random_symble, function_math
import random

class TestMathGame(unittest.TestCase):

    def test_function_random_min_max(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_random_min_max(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_symble(self):
        # TODO
        symbols = ['+', '-', '*']
        result = function_random_symble
        self.assertIsInstance(result, str, f"Expected string, got {type(result)}")

        pass

    def test_function_math(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
                (10, 7, '-', '10-7', 3)
                (4, 8, '*', '4*8', 32)
                (6, 1, '+', '6+1', 7)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                result = function_math(num1, num2, operator)

                # Check the problem string
                self.assertEqual(result[0], expected_problem, f"Problem mismatch for {num1} {operator} {num2}")

                # Check the answer
                self.assertEqual(result[1], expected_answer, f"Answer mismatch for {num1} {operator} {num2}")
                pass

if __name__ == "__main__":
    unittest.main()
