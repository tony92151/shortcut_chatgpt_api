import logging

from flask import Flask, json

from utils import globalDB

api = Flask(__name__)


@api.route("/question", methods=["GET"])
def get_companies():
    if globalDB.question_is_empty():
        return json.dumps({"question": "", "uuid": ""})
    question = globalDB.get_question()
    logging.warning(f"Push question: {question.question}")
    return json.dumps({"question": question.question, "uuid": question.uuid})


def run(host: str = "0.0.0.0", port: int = 9001):
    api.run(host=host, port=port)


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=9001)
