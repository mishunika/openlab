from evaluator import Evaluator


class EvaluatorTest(Evaluator):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    et = EvaluatorTest()
    et.add_coefficient('Test 1', 0.3)
    et.add_coefficient('Test 2', 0)
    et.add_coefficient('Test 3', 0.3)
    et.pass_mandatory_test()

    print(et)
    print(et.coefficients)
    print(et.get_final_score())
