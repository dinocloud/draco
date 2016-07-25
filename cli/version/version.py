import os


def show_version():
    version_file_path = os.path.dirname(os.path.realpath(__file__)) + '/../../version.info'
    with open(version_file_path, 'r') as fin:
        print "Draco client version: {version}".format(version=fin.read())
