from ConfigParser import ConfigParser
DEFAULT_CONFIG_FILE = '/etc/dracoctl/conf/dracoctl.conf'


def get_config_from_file(config_file=DEFAULT_CONFIG_FILE):
    config = ConfigParser()
    config.read(config_file)
    return config.sections()


def get_app_config_from_file(config_file, app_name):
    return get_config_from_file(config_file).get(app_name, {})
