import logging
from abc import ABC

from utils.Utils import LOG


class StepBase(ABC):
    @staticmethod
    def print(message: str):
        LOG(message)
