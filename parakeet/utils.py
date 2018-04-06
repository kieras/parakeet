# -*- coding: utf-8 -*-
import yaml
import os
from lettuce import world

NEXT_IMAGE_SEQUENCE = 'next_image_sequence'


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


def next_image():
    """
    Return the next image number
    :return:
    """

    if world.container.get(NEXT_IMAGE_SEQUENCE, None) is None:
        world.container[NEXT_IMAGE_SEQUENCE] = range_generator()

    return world.container[NEXT_IMAGE_SEQUENCE].next()


def range_generator(max_register=99999):
    """
    Create a generator register
    :return:
    """
    my_list = range(1, max_register)
    for i in my_list:
        yield i
