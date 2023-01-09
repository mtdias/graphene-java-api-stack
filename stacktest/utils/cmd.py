import subprocess
import os


def call_and_wait(cmd, path_dir): return subprocess.check_call(cmd, shell=True, cwd=path_dir)


def call_and_get_output(cmd): return subprocess.check_output(cmd, shell=True, text=True)


def export_env(key, value): os.environ[key] = value


def get_env(key): return os.environ.get(key)
