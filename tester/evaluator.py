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

if __name__ == "__main__":
    e = Evaluator()
    e.add_coefficient('Test 1', 0.3)
    e.add_coefficient('Test 2', 0)
    e.add_coefficient('Test 3', 0.3)

    print(e)
    print(e.coefficients)
    print(e.get_final_score())
