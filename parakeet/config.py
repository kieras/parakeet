import yaml


def load_config(yaml_file):
    print('Loading configs from {0} file.'.format(yaml_file))
    with open(yaml_file, 'r') as config_file:
        config_dict = yaml.load(config_file)
    return config_dict
