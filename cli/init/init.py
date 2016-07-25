import os
import sys
import traceback
import settings
from subprocess import check_call, CalledProcessError

_LOGGER = settings.get_logger()


def init_test_folder(args):
    if args.dir:
        project_path = args.dir
    else:
        project_path = os.getcwd()
    src_path = os.path.dirname(os.path.realpath(__file__)) + "/../tasks"
    make_path = src_path + "/Makefile"

    cmd = "make init -f {make_path} PROJECT_FOLDER={project_path} SOURCE_FOLDER={src_path}"\
        .format(make_path=make_path, project_path=project_path, src_path=src_path)
    try:
        check_call(cmd, shell=True)
    except CalledProcessError as err:
        _LOGGER.error(err.message)
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)