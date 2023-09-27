class Locator(object):
    __name: str
    __automationId: str
    __controlType: str

    def __init__(self, name="", automationId="", controlType=""):
        self.__name = name
        self.__automationId = automationId
        self.__controlType = controlType

    def getName(self):
        return self.__name

    def getAutomationId(self):
        return self.__automationId

    def getControlType(self):
        return self.__controlType


def loc(name="", automationId="", controlType=""):
    return Locator(name=name, automationId=automationId, controlType=controlType)
