from utils.common_message import JSON_UNDEFINED_NODE_ERROR_MESSAGE
from utils.exception import StackTestException


class InputFlags:
    def __init__(self, input_flags_mock_as_json):
        self.__input_flags_mock_as_json = input_flags_mock_as_json
        pass

    def get(self, dynamic_input_flag_key):
        if dynamic_input_flag_key in self.__input_flags_mock_as_json:
            return self.__input_flags_mock_as_json[dynamic_input_flag_key]
        raise StackTestException(
            message=JSON_UNDEFINED_NODE_ERROR_MESSAGE.format(
                node_path=f"exec_configurations.input_flags_mock.{dynamic_input_flag_key}"))

    def get_items(self):
        return self.__input_flags_mock_as_json.items()
