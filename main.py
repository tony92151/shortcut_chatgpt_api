import threading

from utils.api_services import run as run_api_service
from utils.shortcut_answer import run as run_answer_service
from utils.shortcut_question import run as run_question_service


def app1():
    run_api_service(port=9001)


def app2():
    run_answer_service(port=9002)


def app3():
    run_question_service(port=9003)


if __name__ == "__main__":
    t1 = threading.Thread(target=app1)
    t2 = threading.Thread(target=app2)
    t3 = threading.Thread(target=app3)
    t1.start()
    t2.start()
    t3.start()
