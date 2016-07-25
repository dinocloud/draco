import argparse
import version
import settings
import sys
import init
_LOGGER = settings.get_logger()

def setup_arguments_parser():
    parser = argparse.ArgumentParser(description='Valid arguments for dracoctl')
    actions = parser.add_subparsers(help='Valid arguments for dracoctl', dest='action')

    # Version parser
    version_help = "Display dracoctl version"
    actions.add_parser('version', help=version_help)

    # Init parser
    init_parser = actions.add_parser('init', help='Init the draco pipeline folder with default files')
    init_parser.add_argument('--dir', help='Directory to start the pipeline folder')
    return parser


def dispatch_version():
    version.show_version()


def dispatch_init(args):
    init.init_test_folder(args)


def main():
    parser = setup_arguments_parser()
    args = parser.parse_args()
    if args.action == 'version':
        dispatch_version()

    if args.action == 'init':
        dispatch_init(args)

if __name__ == "__main__":
    sys.exit(main())
