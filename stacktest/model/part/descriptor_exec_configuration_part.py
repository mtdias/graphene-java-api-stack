from typing import List

from model.part.descriptor_after_render_part import AfterRender
from model.part.descriptor_input_flags_part import InputFlags
from model.part.descriptor_technology_part import Technology
from utils.common_message import JSON_UNDEFINED_NODE_ERROR_MESSAGE
from utils.exception import StackTestException


class ExecConfigurations:
    def __init__(self, __exec_configuration_as_json):
        self.__exec_configuration_as_json = __exec_configuration_as_json
        self.technologies: List[Technology] = list()
        pass

    def get_technologies(self):
        if not self.technologies:
            if "technologies" in self.__exec_configuration_as_json:
                for technology in self.__exec_configuration_as_json["technologies"]:
                    self.technologies.append(Technology(technology))
        return self.technologies
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.technologies"))

    def get_input_flag(self):
        if "input_flags_mock" in self.__exec_configuration_as_json:
            return InputFlags(self.__exec_configuration_as_json["input_flags_mock"])
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.input_flags_mock"))

    def get_after_render(self):
        if "after_render" in self.__exec_configuration_as_json:
            return AfterRender(self.__exec_configuration_as_json["after_render"])
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path="exec_configurations.after_render"))
