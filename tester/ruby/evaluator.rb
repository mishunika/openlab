class Evaluator
    def initialize
        @coefficients = Array.new
    end

    def add_coefficient(name, value)
        coefficient = {'name': name.to_s, 'value': value.round(2)}
        @coefficients << coefficient
    end

    def get_final_score
        if @coefficients[0] == 0
            return 0.to_f
        end

        score = 0
        @coefficients.each do |c|
            score += c[:value] * 100
        end

        score
    end

    def execute_method(method_name, arguments: Hash.new)
        begin
            if arguments.empty?
                return @solution.send(method_name)
            else
                return @solution.send(method_name, **arguments)
            end
        rescue NameError => boom
            puts "Method not existing"
            return nil
        end
    end

    def method_test(method, tests, reward)
        results = Array.new
        tests.each do |t|
            result = execute_method(method, arguments: t[:"arguments"])
            results << (result == t[:"expected_result"])
        end

        passed = results.reduce{|r,e| r && e}
        coefficient = passed ? reward[:"coefficient"] : 0
        add_coefficient(reward[:"message"], coefficient)
    end

    def get_test_results
        results = {
            'coefficients': @coefficients,
            'score': get_final_score()
        }
        return results
    end
end
