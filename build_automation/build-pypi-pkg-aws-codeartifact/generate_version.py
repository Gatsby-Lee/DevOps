import argparse
import os

from datetime import datetime

commit_subject = os.environ.get("GERRIT_CHANGE_SUBJECT", "unknown")
commit_owner = os.environ.get("GERRIT_CHANGE_OWNER", "unknown")


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--create-version-file", action="store_true")

    return parser.parse_args()


def _main():
    args = _parse_args()

    n = datetime.utcnow()
    vervion_str = n.strftime("%y.%m%d.%H%M%S")
    print(vervion_str)

    if args.create_version_file:
        with open("app/__version__.py", "w") as fw:
            fw.write("# UTC Timezone: <YY>.<MMDD>.<HHMMSS>\n")
            fw.write('__version__ = "%s"\n' % vervion_str)
            fw.write('__commit__ = "%s"\n' % commit_subject)
            fw.write('__owner__ = "%s"\n' % commit_owner)


if __name__ == "__main__":
    _main()
