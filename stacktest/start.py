import re
import sys

from executor.executor import Executor
from utils.arguments import Arguments


def main():
    args = Arguments().parse_args
    plugin_reference = args.plugin_reference
    if plugin_reference:
        if not is_separated_by_comma(plugin_reference):
            print("The plugin directory name should be separated by comma."
                  " EX: plugin1:file1,plugin2:file2,etc")
            sys.exit(1)
        Executor().by_plugin_directory_name(plugin_reference)
    else:
        Executor().all()


def is_separated_by_comma(plugin_reference):
    # TODO Review the regex pattern to accept the following pattern plugin1:file1,plugin2:file2
    return re.search("([a-zA-Z-_]+:[a-zA-Z-_]+,)+([a-zA-Z-_]+:[a-zA-Z-_]+)|([a-zA-Z-_]+:[a-zA-Z-_]+)$",
                     plugin_reference)


main()
