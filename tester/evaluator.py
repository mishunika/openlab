class Evaluator:
    def __init__(self):
        self.mandatory_passed = False
        self.coefficients = []

    def add_coefficient(self, name, value):
        coefficient = {'name': str(name), 'value': round(value, 2)}
        self.coefficients.append(coefficient)

    def pass_mandatory_test(self):
        self.mandatory_passed = True

    def get_final_score(self):
        if not self.mandatory_passed:
            return float(0)
        score = 50
        for coefficient in self.coefficients:
            score += coefficient['value'] * 50
        return score

if __name__ == "__main__":
    e = Evaluator()
    e.add_coefficient('Test 1', 0.3)
    e.add_coefficient('Test 2', 0)
    e.add_coefficient('Test 3', 0.3)
    e.pass_mandatory_test()

    print(e)
    print(e.coefficients)
    print(e.get_final_score())
