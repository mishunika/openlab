import os
import sys

stdout = sys.stdout                 # Backup STDOUT
dev_null = open(os.devnull, 'w')    # /dev/null
sys.stdout = dev_null               # Setting stdout to /dev/null

from evaluator_test import EvaluatorTest

et = EvaluatorTest()
et.run_all_tests()

sys.stdout = stdout                 # Restoring the right stdout
print(et.get_test_results())
