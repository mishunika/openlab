from functools import reduce
from operator import and_ as and_lambda


class Evaluator:
    def __init__(self):
        self.coefficients = []

    def add_coefficient(self, name, value):
        coefficient = {'name': str(name), 'value': round(value, 2)}
        self.coefficients.append(coefficient)

    def get_final_score(self):
        if self.coefficients[0]['value'] == 0:
            return float(0)

        score = 0
        for coefficient in self.coefficients:
            score += coefficient['value'] * 100
        return score

    def execute_method(self, method_name, arguments={}):
        try:
            method_ref = getattr(self.solution, method_name)
            result = method_ref(**arguments)
        except AttributeError as e:
            print(e)
            return None

        return result

    def method_test(self, method, tests, reward):
        results = []
        for test in tests:
            result = self.execute_method(method, test['arguments'])
            results.append(result == test['expected_result'])
        passed = reduce(and_lambda, results)
        coefficient = reward['coefficient'] if passed else 0
        self.add_coefficient(reward['message'], coefficient)


if __name__ == "__main__":
    e = Evaluator()
    e.add_coefficient('Test 1', 0.3)
    e.add_coefficient('Test 2', 0)
    e.add_coefficient('Test 3', 0.3)

    print(e)
    print(e.coefficients)
    print(e.get_final_score())
