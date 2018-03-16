# -*- coding: utf-8 -*-
import yaml
import os

def load_yaml(yaml_file):
    """
    Load a YAML file and return it as a dict.

    :param yaml_file: path to the yaml file.
    :type yaml_file: str
    :return: a dict.
    """
    _local_file = os.path.join(os.path.expanduser('~'), yaml_file)
    _local_file = _local_file if os.path.exists(_local_file) else yaml_file

    print('Loading file: {}.'.format(_local_file))
    with open(_local_file, 'r') as f:
        yaml_content = yaml.load(f)
    return yaml_content
