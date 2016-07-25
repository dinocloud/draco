import os
import settings

_LOGGER = settings.get_logger()

def show_version():
    version_file_path = os.path.dirname(os.path.realpath(__file__)) + '/../../version.info'
    with open(version_file_path, 'r') as fin:
        _LOGGER.info("Draco client version: {version}".format(version=fin.read()))
