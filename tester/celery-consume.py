from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue
from docker import Docker
import psycopg2
import json


class CustomConsumerStep(bootsteps.ConsumerStep):
    queue = Queue('default', Exchange('default'), 'default')

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[self.queue],
                         callbacks=[self.handle_message],
                         accept=['pickle', 'json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        submission_id = body['args'][0]
        test_f, sol_f, lang = get_test_and_solution(submission_id)

        docker = Docker()
        test = open('/app/evaluator_tests/' + test_f)
        solution = open('/app/evaluator_submissions/' + sol_f)
        out = docker.run(lang, test, solution)
        metadata = json.loads(out)
        try:
            if metadata['score']:
                status = 'P'
            else:
                status = 'F'

            score = metadata['score']
        except KeyError:
            status = 'F'
            score = 0

        if update_submission(submission_id, score, out, status):
            message.ack()


# TODO: Use env variables for RabbitMQ credentials
app = Celery(broker='amqp://guest:guest@rabbit//')
app.steps['consumer'].add(CustomConsumerStep)


def get_conn():
    # TODO: Use env variables for PostgreSQL credentials
    conn = psycopg2.connect(database="postgres", user="postgres", host="db")
    return conn


def get_test_lang(filename, short=True):
    langs = {
        'py': {'short': 'P', 'long': 'python'},
        'rb': {'short': 'R', 'long': 'ruby'}}
    ext = filename[-2:]
    res_type = 'short' if short else 'long'
    try:
        return langs[ext][res_type]
    except KeyError:
        return 'P'


def get_test_and_solution(submission_id):
    conn = get_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("SELECT assignment_id, file \
                FROM evaluator_submission WHERE id=%s", (submission_id,))
    submission = cur.fetchone()

    langs = {'py': 'P', 'rb': 'R'}
    submission_ext = submission[1][-2:]
    try:
        lang = langs[submission_ext]
    except KeyError:
        lang = 'P'

    lang = get_test_lang(submission[1])
    lang_full = get_test_lang(submission[1], short=False)

    cur.execute("SELECT file \
                FROM evaluator_testcase \
                WHERE assignment_id=%s AND lang=%s", (submission[0], lang,))
    testcase = cur.fetchone()

    cur.close()
    conn.close()
    return testcase[0], submission[1], lang_full


def update_submission(id, score, metadata, status):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE evaluator_submission \
                SET score=%s, metadata=%s, status=%s \
                WHERE id=%s", (score, metadata, status, id))
    conn.commit()
    status = cur.statusmessage
    cur.close()
    conn.close()
    return True if status else False
