from json import JSONEncoder

from helper.executor_helper import *
from model.descriptor_object import DescriptorObject
from model.part.descriptor_apply_plugin import ApplyPlugin
from model.part.descriptor_exec_configuration_part import ExecConfigurations
from utils.exception import StackTestException
from utils.paths import *


class DescriptorEncoder(JSONEncoder):
    def default(self, o): return o.__dict__


class Executor:
    def __init__(self):
        self.__descriptor = None
        pass

    def all(self):
        try:
            recreate_test_output_directory(TEST_OUTPUT_PATH)
            for descriptor_path in get_all_descriptor_file_paths(DESCRIPTOR_FILE_PATH):
                print(f"Reading description file {descriptor_path}")
                descriptor_as_dict = get_descriptor_json_by_path(descriptor_path)
                self.__execute_test(DescriptorObject(descriptor_as_dict))
        except StackTestException as ex:
            """
            Criar mensagem: Falha ao executar o teste do plugin [DIRETÓRIO]
            """
            print(ex.get_message())
            raise ex

    def by_plugin_directory_name(self, plugin_reference):
        index_plugin_name = 0
        index_plugin_test_file = 1
        try:
            recreate_test_output_directory(TEST_OUTPUT_PATH)
            for plugin_name in plugin_reference.split(","):
                split_plugin_reference_name = plugin_name.split(":")
                plugin_name = split_plugin_reference_name[index_plugin_name]
                file_name = split_plugin_reference_name[index_plugin_test_file]
                descriptor_path = DESCRIPTOR_FILE_PATH.replace("../*/test/*-test.json",
                                                               f"../{plugin_name}/test/{file_name}.json")
                descriptor_as_dict = get_descriptor_json_by_path(descriptor_path)
                self.__execute_test(DescriptorObject(descriptor_as_dict))
        except StackTestException as ex:
            raise ex
        except Exception as ex:
            print(f"Error executing the method by_plugin_directory_name {ex}")
            raise ex

    def __execute_test(self, descriptor_object: DescriptorObject):
        for configs in descriptor_object.exec_configurations():
            if is_environment_technology(configs):
                generated_application_path = create_app(configs, descriptor_object.base_plugin_name(), TEST_OUTPUT_PATH)

                self.__execute_apply_plugin_if_exists(configs)

                execute_build_commands(configs, generated_application_path)

                self.__execute_test_instructions(configs, generated_application_path)

                print(f"Project {configs.get_input_flag().get('project_name')} validated successfully")

    def __execute_apply_plugin_if_exists(self, configs: ExecConfigurations):
        if configs.get_after_render().get_apply_plugin():
            apply_plugin(configs)
        return self

    def __execute_test_instructions(self, configs: ExecConfigurations, generated_application_path):
        test_instructions = configs.get_after_render().get_test_instructions()
        try:
            for instruction in test_instructions:
                response = execute_test_command(instruction.get_command())

                contains_result_as_json(instruction, response)

                not_contains_result_as_json(instruction, response)

                not_contains_texts(instruction, response)
        finally:
            after_test_commands(configs, generated_application_path)
        return self
