import logging

from flask import Flask, json, request

from utils import globalDB
from utils.db import Answer

api = Flask(__name__)


@api.route("/answer", methods=["POST"])
def pet_question():
    logging.warning(request.is_json)
    if request.is_json:
        data = request.get_json()
        answer = data.get("answer", None)
        uuid_ = data.get("uuid", None)
        if answer is None or uuid_ is None or uuid_ == "":
            return json.dumps({"success": False})
        logging.info(answer)
        if answer:
            logging.warning(f"Get answer: {answer}")
            globalDB.write_answer(Answer(answer, uuid_))
            return json.dumps({"success": True})
    return json.dumps({"success": False})


def run(host: str = "0.0.0.0", port: int = 9001):
    api.run(host=host, port=port)


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=9001)
