class StackTestException(RuntimeError):
    def __init__(self, **kwargs):
        self.__exception = self.__get_arg("exception", kwargs)
        self.__message = self.__get_arg("message", kwargs)

        if self.__exception and self.__message:
            super(RuntimeError, self).__init__(self.__message, self.__exception)
        else:
            super(RuntimeError, self).__init__(self.__message)

    def __get_arg(self, arg, kwargs):
        if arg in kwargs:
            return kwargs[arg]
        return None

    def get_message(self):
        return self.__message

    def get_exception(self):
        return self.__exception
