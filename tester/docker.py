from argparse import ArgumentParser
from subprocess import Popen, PIPE
import os


class Docker:
    def build(self, image):
        if not self.dockerfile_exists(image):
            return False
        # docker build -t openlab/python ./python
        p = Popen(['docker', 'build', '-t', 'openlab/' + image,
                   './' + image], stdout=PIPE)
        p.communicate()
        return not p.returncode

    def dockerfile_exists(self, image):
        img_dir = './' + image
        img_dockerfile = img_dir + '/Dockerfile'
        if os.path.isdir(img_dir) and os.path.isfile(img_dockerfile):
            return True
        return False

    def kill_and_remove(self, ctr_name):
        for action in ('kill', 'rm'):
            p = Popen('docker %s %s' % (action, ctr_name), shell=True,
                      stdout=PIPE, stderr=PIPE)
            if p.wait() != 0:
                raise RuntimeError(p.stderr.read())

    def run(self, image, test, solution):
        test_volume = self.volume_for_file(test, test=True)
        solution_volume = self.volume_for_file(solution, test=False)

        ctr_name = 'thesis_stashed_tester'
        p = Popen(['timeout', '-s', 'SIGKILL', '10',
                   'docker', 'run', '--rm', '--name', ctr_name,
                   '-v', test_volume,
                   '-v', solution_volume,
                   'openlab/' + image],
                  stdout=PIPE)
        out = p.stdout.read()

        if p.wait() == -9:  # Happens on timeout
            # We have to kill the container since it still runs
            # detached from Popen and we need to remove it after because
            # --rm is not working on killed containers
            self.kill_and_remove(ctr_name)

        return bytes.decode(out)

    def volume_for_file(self, f, test=True):
        n = f.name
        destination = "solution.py"
        if test:
            destination = "evaluator_test.py"

        return os.path.abspath(n) + ':' + '/app/' + destination + ':ro'


class CLI:
    def __init__(self):
        self.docker = Docker()

    def execute(self, args):
        if args.action == 'build':
            success = self.docker.build(args.image_type)
            if success:
                print('The image was built successfully.')
            else:
                print('I can not build it.')
        elif args.action == 'run':
            out = self.docker.run(args.image_type, args.test, args.solution)
            print(out)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("action", type=str,
                        help="the command that we intend to run")
    parser.add_argument("image_type", type=str,
                        help="the image type. ex: python, ruby...")
    parser.add_argument("-t", "--test", type=open,
                        help="test source file")
    parser.add_argument("-s", "--solution", type=open,
                        help="solution source file")

    args = parser.parse_args()

    cli = CLI()
    cli.execute(args)
