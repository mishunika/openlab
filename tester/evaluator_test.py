from evaluator import Evaluator
from solution import Solution


class EvaluatorTest(Evaluator):
    def __init__(self):
        super().__init__()
        self.solution = Solution()

    def check_result(self, expected, result, coefficient):
        return coefficient if result is expected else 0

    def run_all_tests(self):
        self.test_mandatory()
        self.test_one()
        self.test_s_two()
        self.test_sum()

    def test_mandatory(self):
        tests = [
            {
                'arguments': {},
                'expected_result': True
            }
        ]
        reward = {
            'message': 'Mandatory test.',
            'coefficient': 0.5
        }
        self.method_test('mandatory', tests, reward)

    def test_one(self):
        tests = [
            {
                'arguments': {},
                'expected_result': 1
            }
        ]
        reward = {
            'message': 'Test one. Should return integer 1',
            'coefficient': 0.1
        }
        self.method_test('one', tests, reward)

    def test_s_two(self):
        tests = [
            {
                'arguments': {},
                'expected_result': '2'
            }
        ]
        reward = {
            'message': 'Test one. Should return str 2',
            'coefficient': 0.1
        }
        self.method_test('s_two', tests, reward)

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
            'message': 'Test #3. Method sum',
            'coefficient': 0.3
        }
        self.method_test('sum', tests, reward)


if __name__ == '__main__':
    et = EvaluatorTest()
    et.run_all_tests()

    print(et)
    print(et.coefficients)
    print(et.get_final_score())
