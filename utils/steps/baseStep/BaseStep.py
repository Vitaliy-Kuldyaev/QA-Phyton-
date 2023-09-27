from utils.Utils import LOG
from utils.steps.StepBase import StepBase


class BaseStep(StepBase):
    @staticmethod
    def printMethod():
        LOG("Print From step")
