from model.part.descriptor_apply_plugin import ApplyPlugin
from model.part.descriptor_test_instructions_part import TestInstructions
from utils.common_message import JSON_UNDEFINED_NODE_ERROR_MESSAGE
from utils.exception import StackTestException


class AfterRender:

    def __init__(self, after_render_as_json):
        self.__after_render_as_json = after_render_as_json
        self.__test_instructions: list[TestInstructions] = list()

    def get_apply_plugin(self):
        if "apply_plugin" in self.__after_render_as_json:
            return ApplyPlugin(self.__after_render_as_json["apply_plugin"])
        return None

    def get_build_commands(self):
        if "build_commands" in self.__after_render_as_json:
            return self.__after_render_as_json["build_commands"]
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.after_render.build_commands"))

    def get_test_instructions(self):
        if not self.__test_instructions:
            if "test_instructions" in self.__after_render_as_json:
                for test_instruction in self.__after_render_as_json["test_instructions"]:
                    self.__test_instructions.append(TestInstructions(test_instruction))
        return self.__test_instructions
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.after_render.test_instructions"))

    def get_after_test_commands(self):
        if "after_test_commands" in self.__after_render_as_json:
            return self.__after_render_as_json["after_test_commands"]
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.after_render.after_test_commands"))
