class Technology:
    def __init__(self, technology_as_json):
        self.__technology_as_json = technology_as_json
        self.__name = technology_as_json["name"]
        self.__version = self.__get_version_if_present()
        pass

    def __get_version_if_present(self):
        return None if "version" not in self.__technology_as_json else self.__technology_as_json["version"]

    def get_name(self):
        return self.__name

    def get_version(self):
        return self.__version

    def __eq__(self, other):
        if other.get_name() == self.__name \
                and other.get_version() == self.__version:
            return True
        return False
