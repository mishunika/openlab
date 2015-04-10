from subprocess import Popen, PIPE
import os


def kill_and_remove(ctr_name):
    for action in ('kill', 'rm'):
        p = Popen('docker %s %s' % (action, ctr_name), shell=True,
                  stdout=PIPE, stderr=PIPE)
        if p.wait() != 0:
            raise RuntimeError(p.stderr.read())


def execute():
    path = os.path.dirname(os.path.realpath(__file__))
    ctr_name = 'thesis_stashed_tester'
    p = Popen(['gtimeout', '-s', 'SIGKILL', '5',
               'docker', 'run', '--rm', '--name', ctr_name,
               '-v', path + '/python/evaluator_test.py:/app/evaluator_test.py',
               '-v', path + '/python/solution.py:/app/solution.py',
               'mishunika/thesis_tester:0.0.1'],
              stdout=PIPE)
    out = p.stdout.read()

    if p.wait() == -9:  # Happens on timeout
        # We have to kill the container since it still runs
        # detached from Popen and we need to remove it after because
        # --rm is not working on killed containers
        kill_and_remove(ctr_name)

    return bytes.decode(out)

print(execute())
