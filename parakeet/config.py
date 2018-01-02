# -*- coding: utf-8 -*-
import yaml


def load_config(yaml_file):
    """
    Load a YAML file and return it as a dict.

    :param yaml_file: path to the yaml file.
    :type yaml_file: str
    :return: a dict.
    """
    print('Loading configs from {0} file.'.format(yaml_file))
    with open(yaml_file, 'r') as config_file:
        config_dict = yaml.load(config_file)
    return config_dict
