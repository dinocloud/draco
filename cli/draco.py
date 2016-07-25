import argparse
import version

def dispatch_version(args):
    version.show_version()

def main():
    parser = argparse.ArgumentParser(description='Valid arguments for dracoctl')
    parser.add_argument('--version', help='Display the version for the dracoctl command', action='store_true')
    args = parser.parse_args()

    if args.version:
        dispatch_version(args)

if __name__ == "__main__":
    main()
