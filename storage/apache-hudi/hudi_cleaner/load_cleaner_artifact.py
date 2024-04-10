"""
@author Gatsby Lee
@since 2024-04-10

## ref
- https://avro.apache.org/docs/1.11.1/getting-started-python/#:~:text=A%20package%20called%20%E2%80%9Cavro%2Dpython3,the%20%E2%80%9Cavro%E2%80%9D%20package%20instead.
- https://www.perfectlyrandom.org/2019/11/29/handling-avro-files-in-python/
"""

import argparse
import copy
import json
import logging
from pprint import pprint
from urllib.request import urlopen

import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader

# from avro.datafile import DataFileReader

LOGGER = logging.getLogger(__name__)

# e.g. "https://github.com/apache/hudi/tree/release-0.12.1/hudi-common/src/main/avro"
# @note: the content has a comment at the top.
AVRO_SCHEMA_PATH_IN_GITHUB = "https://raw.githubusercontent.com/apache/hudi/release-%(version)s/hudi-common/src/main/avro/%(filename)s"

AVRO_SCHEMA_FILENAME_CLEANER_METADATA = "HoodieCleanMetadata.avsc"
AVRO_SCHEMA_FILENAME_CLEANER_PART_METADATA = "HoodieCleanPartitionMetadata.avsc"
AVRO_SCHEMA_FILENAME_CLEANER_PLAN = "HoodieCleanerPlan.avsc"


def get_avro_schema(link):
    f = urlopen(link)
    avro_schema_raw = f.read().decode()
    avro_schema = avro.schema.parse(avro_schema_raw)
    return avro_schema


def get_avro_schema_download_uri(version: str, filename: str):
    uri = AVRO_SCHEMA_PATH_IN_GITHUB % {"version": version, "filename": filename}
    return uri


def process_loading(cleaner_filename: str):
    with open(cleaner_filename, "rb") as f:
        reader = DataFileReader(f, DatumReader())
        ## get content
        # print(reader.meta)
        # print(reader.block_count)
        print("===================== SCHEMA!!")
        pprint(json.loads(reader.schema))
        print("\n\n\n\n===================== CONTENT!!")
        for x in reader:
            pprint(x)

        reader or reader.close()


def _parse_args():
    base_parser = argparse.ArgumentParser(add_help=False)
    # base_parser.add_argument("--release-ver", required=True)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="action", required=True)

    cmd_plan = subparser.add_parser("plan", parents=[base_parser])
    cmd_plan.add_argument("--plan-filename", required=True)

    return parser.parse_args()


def main():
    """
    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240328130711679.clean.requested

    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240410095913967.clean.requested
    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240410095913967.clean.inflight
    python load_cleaner_artifact.py plan \
        --plan-filename ~/Downloads/20240410095913967.clean
    """
    args = _parse_args()

    if args.action == "plan":
        process_loading(args.plan_filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
