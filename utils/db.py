import queue
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Question:
    question: str
    uuid: str


@dataclass
class Answer:
    answer: str
    uuid: str


class DB:
    def __init__(self):
        self._question_memory = queue.Queue(maxsize=10)
        self._answer_memory = queue.Queue(maxsize=100)

    def question_is_empty(self) -> bool:
        return self._question_memory.empty()

    def get_question(self):
        return self._question_memory.get()

    def get_answer(self, uuid_: str) -> (bool, str):
        memory = deepcopy(list(self._answer_memory.queue))
        for data in memory:
            if data.uuid == uuid_:
                return True, data.answer
        return False, ""

    def write_question(self, question: Question):
        self._question_memory.put(question)

    def write_answer(self, answer: Answer):
        self._answer_memory.put(answer)
