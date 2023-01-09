from model.part.descriptor_exec_configuration_part import *
from utils.common_message import JSON_UNDEFINED_NODE_ERROR_MESSAGE
from utils.exception import StackTestException


class DescriptorObject:
    def __init__(self, descriptor_as_json):
        self.__descriptor_as_json = descriptor_as_json
        self.__exec_configurations: list[ExecConfigurations] = list()
        pass

    def base_plugin_name(self):
        if "base_plugin" in self.__descriptor_as_json:
            return self.__descriptor_as_json["base_plugin"]
        raise StackTestException(message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(node_path="base_plugin"))

    def exec_configurations(self):
        if not self.__exec_configurations:
            if "exec_configurations" in self.__descriptor_as_json:
                for exec_configuration in self.__descriptor_as_json["exec_configurations"]:
                    self.__exec_configurations.append(ExecConfigurations(exec_configuration))
        return self.__exec_configurations
        raise StackTestException(message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(node_path="exec_configurations"))

