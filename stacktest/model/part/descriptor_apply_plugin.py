from model.part.descriptor_input_flags_part import InputFlags
from utils.common_message import JSON_UNDEFINED_NODE_ERROR_MESSAGE
from utils.exception import StackTestException


class ApplyPlugin:
    def __init__(self, apply_plugin_as_json):
        self.__apply_plugin_as_json = apply_plugin_as_json

    def get_plugin_name(self):
        if "plugin_name" in self.__apply_plugin_as_json:
            return self.__apply_plugin_as_json["plugin_name"]
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path=f"exec_configurations.after_render.apply_plugin.plugin_name"))

    def get_input_flags(self):
        if "input_flags_mock" in self.__apply_plugin_as_json:
            return InputFlags(self.__apply_plugin_as_json["input_flags_mock"])
        return InputFlags({})
