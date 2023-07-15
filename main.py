import threading

from utils.api_services import run as run_api_service
from utils.shortcut_connector import run as run_shortcut_connector


def app1():
    run_api_service(port=9001)


def app2():
    run_shortcut_connector(port=9002)


if __name__ == "__main__":
    t1 = threading.Thread(target=app1)
    t2 = threading.Thread(target=app2)
    t1.start()
    t2.start()
