from collections import namedtuple
from json import load
from pathlib import Path


def get_conf(json_file="conf"):
    """Returns the configuration from the config file

    Args:
        json_file (str, optional): Name of the config file (without file type). Defaults to "conf".
    Returns:
        object: A python object
    """
    full_path = Path(__file__).parent.absolute()
    with open(Path(full_path, "config", f"{json_file}.json"), "r") as conf:
        return load(conf, object_hook=lambda d: namedtuple("hosts", d.keys())(*d.values()))
