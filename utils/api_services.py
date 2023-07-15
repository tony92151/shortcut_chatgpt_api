import logging
import time
import uuid

from flask import Flask, json, request

from utils import globalDB
from utils.db import Question

api = Flask(__name__)


def get_uuid():
    return str(uuid.uuid4())


@api.route("/question", methods=["POST"])
def pet_question_and_wait_for_answer():
    if not request.is_json:
        return json.dumps({"success": False, "answer": ""})

    data = request.get_json()
    question = data.get("question", None)

    if question is None:
        return json.dumps({"success": False, "answer": ""})

    logging.warning(f"Get question: {question}")
    uuid_ = get_uuid()
    globalDB.write_question(Question(question, uuid_))

    start_time = time.time()
    while True:
        time.sleep(0.2)
        found, ans = globalDB.get_answer(uuid_=uuid_)
        if found:
            return json.dumps({"success": True, "answer": ans})
        if time.time() - start_time > 60:
            return json.dumps({"success": False, "answer": ""})


def run(host: str = "0.0.0.0", port: int = 9001):
    api.run(host=host, port=port)


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=9001)
