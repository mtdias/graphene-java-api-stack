from utils.common_message import JSON_UNDEFINED_NODE_ERROR_MESSAGE
from utils.exception import StackTestException


class TestInstructions:
    def __init__(self, test_instructions_as_json):
        self.__test_instructions_as_json = test_instructions_as_json

    def get_command(self):
        if "command" in self.__test_instructions_as_json:
            return self.__test_instructions_as_json["command"]
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.after_render.test_instructions.command"))

    def get_contains_result_as_json(self):
        if "contains_result_as_json" in self.__test_instructions_as_json:
            return self.__test_instructions_as_json["contains_result_as_json"]
        return {}

    def get_not_contains_result_as_json(self):
        if "not_contains_result_as_json" in self.__test_instructions_as_json:
            return self.__test_instructions_as_json["not_contains_result_as_json"]
        return {}

    def get_not_contains_texts(self):
        if "not_contains_texts" in self.__test_instructions_as_json:
            return self.__test_instructions_as_json["not_contains_texts"]
        return []
