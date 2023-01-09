import glob
import json
import re
import shutil

from model.part.descriptor_apply_plugin import ApplyPlugin
from model.part.descriptor_exec_configuration_part import ExecConfigurations
from model.part.descriptor_input_flags_part import InputFlags
from model.part.descriptor_technology_part import Technology
from model.part.descriptor_test_instructions_part import TestInstructions
from utils.cmd import *
from utils.exception import StackTestException
from utils.paths import TEST_OUTPUT_PATH


def get_all_descriptor_file_paths(pattern_descriptor_file_path):
    """
    @:param pattern_descriptor_file_path Ex: ../../*/test/*-test.json
    @:return list of descriptor files path
    """
    try:
        return glob.glob(pattern_descriptor_file_path)
    except Exception as ex:
        raise StackTestException(message="Error to get the file path descriptor test in get_all_descriptor_file_paths",
                                 exception=ex)


def get_single_descriptor_file_paths(descriptor_file_path):
    """
    @:param descriptor_file_path Ex: ../../plugin-folder/test/plugin-descriptor-test.json
    @:return list of descriptor files path
    """
    try:
        return glob.glob(descriptor_file_path)
    except Exception as ex:
        raise StackTestException(
            message="Error to get the file path descriptor test in method get_single_descriptor_file_paths",
            exception=ex)


def get_descriptor_json_by_path(descriptor_path):
    try:
        with open(descriptor_path, 'r') as file_as_json:
            return json.load(file_as_json)
    except Exception as ex:
        raise StackTestException(message="Error in get_descriptor_json_by_path. Check if the descriptor file exists or "
                                         "is according to json specification",
                                 exception=ex)


def recreate_test_output_directory(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)
    except Exception as ex:
        raise StackTestException(message="Error during recreate test output directory", exception=ex)


def build_input_flags(flags_mock: InputFlags):
    try:
        input_flags = []
        for key, value in flags_mock.get_items():
            if key != "project_name":
                input_flags.append(f"--{key} {value}")
        return input_flags
    except Exception as ex:
        raise StackTestException(message="Error during building input flags", exception=ex)


def mount_create_app_command(configs: ExecConfigurations, base_plugin_name):
    try:
        flags_mock = configs.get_input_flag()

        return "stk create app {project_name} -p ../../{base_plugin} {input_flags}" \
            .format(project_name=flags_mock.get("project_name"),
                    base_plugin=base_plugin_name,
                    input_flags=" ".join(build_input_flags(flags_mock)))
    except Exception as ex:
        raise StackTestException(message="Error during mounting the create app command", exception=ex)


def is_environment_technology(configs: ExecConfigurations):
    """Check if the test scenery is equivalent to the current node of the descriptor test file"""
    if get_env("ENVIRONMENT_TECHNOLOGIES"):
        environment_technologies: list[Technology] = list(map(lambda env_tech: Technology(env_tech),
                                                              json.loads(get_env("ENVIRONMENT_TECHNOLOGIES"))))
        for config_tech in configs.get_technologies():
            if not environment_technologies.__contains__(config_tech):
                return False
    return True


def create_app(configs: ExecConfigurations, base_plugin_name, test_output_path):
    try:
        create_app_command = mount_create_app_command(configs, base_plugin_name)
        call_and_wait(create_app_command, test_output_path)
        return get_generated_application_path(configs, test_output_path)
    except Exception as ex:
        raise StackTestException(message="Error during execution the create app command", exception=ex)


def apply_plugin(configs: ExecConfigurations):
    try:
        apply_plugin_obj: ApplyPlugin = configs.get_after_render().get_apply_plugin()
        input_flags_plugin: InputFlags = apply_plugin_obj.get_input_flags()

        apply_plugin_command = "stk apply plugin -p ../../../{plugin_name} {input_flags}" \
            .format(plugin_name=apply_plugin_obj.get_plugin_name(),
                    input_flags=" ".join(build_input_flags(input_flags_plugin)))

        project_name = configs.get_input_flag().get("project_name")

        call_and_wait(apply_plugin_command, f"{TEST_OUTPUT_PATH}/{project_name}")

        print(f"Plugin {apply_plugin_obj.get_plugin_name()} applied successfully")
    except Exception as ex:
        raise StackTestException(message=f"Error applying plugin {apply_plugin_obj.get_plugin_name()} "
                                         f" for the project {project_name}", exception=ex)


def get_generated_application_path(configs: ExecConfigurations, test_output_path):
    try:
        return f"{test_output_path}/{configs.get_input_flag().get('project_name')}"
    except Exception as ex:
        raise StackTestException(message="Error retrieving the generated application path", exception=ex)


def execute_build_commands(configs: ExecConfigurations, application_path):
    try:
        build_commands = configs.get_after_render().get_build_commands()
        for build_command in build_commands:
            print(f"Executing command {build_command}")
            call_and_wait(build_command, path_dir=application_path)
    except Exception as ex:
        raise StackTestException(message="Error executing the application build commands", exception=ex)


def execute_test_command(command):
    try:
        print(f"Executing command {command} in execute_test_command method")
        response = json.loads(call_and_get_output([command]))
        print(f"Response {response}")
        return response
    except Exception as ex:
        raise StackTestException(message="Error executing the application test command", exception=ex)


def contains_result_as_json(test_instructions: TestInstructions, response):
    try:
        result_as_json_obj = test_instructions.get_contains_result_as_json()
        for key, value in result_as_json_obj.items():
            if not response[key] == value:
                raise AssertionError(f"Contains_result_as_json error. The {key}:{value} "
                                     f"is not present in the response command")
        if result_as_json_obj:
            print("contains_result_as_json validated successfully")
    except Exception as ex:
        raise StackTestException(message="Error during executing validation contains_result_as_json",
                                 exception=ex)


def not_contains_result_as_json(test_instructions: TestInstructions, response):
    try:
        not_contains_result_obj = test_instructions.get_not_contains_result_as_json()
        for key, value in not_contains_result_obj.items():
            if response[key] == value:
                raise AssertionError(f"not_contains_result_array error. The {key}:{value} shouldn't be present"
                                     f" in the response of the test command execution")
        if not_contains_result_obj:
            print("not_contains_result_array validated successfully")
    except Exception as ex:
        raise StackTestException(message="Error during executing validation not_contains_result_as_json",
                                 exception=ex)


def not_contains_texts(test_instructions: TestInstructions, response):
    try:
        not_contains_text_array = test_instructions.get_not_contains_texts()
        for text in not_contains_text_array:
            if re.search(text, json.dumps(response)):
                raise AssertionError(f"not_contains_texts error. The value {text} shouldn't " \
                                     f"be present in the response of the test command execution")
        if not_contains_text_array:
            print("not_contains_texts validated successfully")
    except Exception as ex:
        raise StackTestException(message="Error during executing validation not_contains_texts",
                                 exception=ex)


def after_test_commands(configs: ExecConfigurations, generated_application_path):
    try:
        commands = configs.get_after_render().get_after_test_commands()
        for command in commands:
            call_and_wait(command, generated_application_path)
    except Exception as ex:
        raise StackTestException(message="Error during executing after_test_commands",
                                 exception=ex)
