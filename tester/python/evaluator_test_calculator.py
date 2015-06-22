from evaluator import Evaluator
from solution import Solution


class EvaluatorTest(Evaluator):
    def __init__(self):
        super().__init__()
        self.solution = Solution()

    def run_all_tests(self):
        self.test_sum()
        self.test_sub()
        self.test_mul()
        self.test_pow()

    def test_sum(self):
        tests = [
            {
                'arguments': {'a': 1, 'b': 1},
                'expected_result': 2
            },
            {
                'arguments': {'a': -1, 'b': 1},
                'expected_result': 0
            },
            {
                'arguments': {'a': 0.1, 'b': 1.2},
                'expected_result': 1
            },
            {
                'arguments': {'a': -5, 'b': -9},
                'expected_result': -14
            },
        ]
        reward = {
            'message': 'Test #1. Method sum',
            'coefficient': 0.2
        }
        self.method_test('sum', tests, reward)

    def test_sub(self):
        tests = [
            {
                'arguments': {'a': 10, 'b': 1},
                'expected_result': 9
            },
            {
                'arguments': {'a': -1, 'b': 1},
                'expected_result': -2
            },
            {
                'arguments': {'a': -5, 'b': -9},
                'expected_result': 4
            },
        ]
        reward = {
            'message': 'Test #2. Method sub',
            'coefficient': 0.25
        }
        self.method_test('sub', tests, reward)

    def test_mul(self):
        tests = [
            {
                'arguments': {'a': 10, 'b': 1},
                'expected_result': 10
            },
            {
                'arguments': {'a': 0, 'b': 1},
                'expected_result': 0
            },
            {
                'arguments': {'a': -5, 'b': -9},
                'expected_result': 45
            },
        ]
        reward = {
            'message': 'Test #3. Method mul',
            'coefficient': 0.25
        }
        self.method_test('mul', tests, reward)

    def test_pow(self):
        tests = [
            {
                'arguments': {'a': 1, 'b': 10},
                'expected_result': 1
            },
            {
                'arguments': {'a': 0, 'b': 1},
                'expected_result': 0
            },
            {
                'arguments': {'a': 10, 'b': 0},
                'expected_result': 1
            },
        ]
        reward = {
            'message': 'Test #4. Method pow',
            'coefficient': 0.3
        }
        self.method_test('pow', tests, reward)