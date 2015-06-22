require 'json'
def silence
	begin
		orig_stderr = $stderr.clone
		orig_stdout = $stdout.clone
		$stderr.reopen File.new('/dev/null', 'w')
		$stdout.reopen File.new('/dev/null', 'w')
		retval = yield
	rescue Exception => e
		$stdout.reopen orig_stdout
		$stderr.reopen orig_stderr
		raise e
	ensure
		$stdout.reopen orig_stdout
		$stderr.reopen orig_stderr
	end
	retval
end

results = nil

silence do
	require_relative 'evaluator_test'

	et = EvaluatorTest.new
	et.run_all_tests
	results = et.get_test_results
end

puts results.to_json
