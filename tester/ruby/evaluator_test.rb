require_relative 'evaluator'
require_relative 'solution'

class EvaluatorTest < Evaluator
    def initialize
        super()
        @solution = Solution.new
    end

    def run_all_tests
        test_mandatory
        test_one
        test_s_two
        test_sum
    end

    def test_mandatory
        tests = [
            {
                'arguments': {},
                'expected_result': true
            }
        ]
        reward = {
            'message': 'Mandatory test.',
            'coefficient': 0.5
        }
        method_test('mandatory', tests, reward)
    end

    def test_one
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
        method_test('one', tests, reward)
    end

    def test_s_two
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
        method_test('s_two', tests, reward)
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
            'message': 'Test #3. Method sum',
            'coefficient': 0.3
        }
        method_test('sum', tests, reward)
    end
end