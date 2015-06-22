require_relative 'evaluator'
require_relative 'solution'

class EvaluatorTest < Evaluator
    def initialize
        super()
        @solution = Solution.new
    end

    def run_all_tests
        test_sum
        test_sub
        test_mul
        test_pow
    end

    def test_sum
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
        method_test('sum', tests, reward)
    end


    def test_sub
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
        method_test('sub', tests, reward)
    end

    def test_mul
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
        method_test('mul', tests, reward)
    end

    def test_pow
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
        method_test('pow', tests, reward)
    end
end