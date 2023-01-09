import argparse


class Arguments:
    __arguments = None

    def __init__(self):
        self.__parse = self.__set_arguments_script_test()
        self.parse_args = self.__parse.parse_args()

    # Singleton instance class
    @staticmethod
    def get_instance():
        if not Arguments.__arguments:
            Arguments.__arguments = Arguments()
        return Arguments.__arguments

    def __set_arguments_script_test(self) -> argparse.ArgumentParser:
        parse = argparse.ArgumentParser(description="arguments test execution")
        parse.add_argument("-r", "--plugin_reference", help="Inform the plugin name and the file to be tested."
                                                            " Ex: plugin1:file1,plugin2:file2")
        return parse
