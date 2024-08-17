"""
compare two different hudi properties
"""

import logging
import sys

from prettytable import PrettyTable

LOGGER = logging.getLogger(__name__)


def parse_content(content: str) -> dict[str, str]:

    parsed_content = {}
    for row in content.split("\n"):
        if row.startswith("#") or not row:
            continue

        k, v = row.strip().split("=")
        parsed_content[k] = v

    return parsed_content


def format_data(config_filename_1: str, config_filename_2: str, content_config_1: str, content_config_2: str):

    all_keys = sorted(list(set(content_config_1.keys()) | set(content_config_2.keys())))
    data = []
    for k in all_keys:
        v1 = content_config_1.get(k, "N/A")
        v2 = content_config_2.get(k, "N/A")
        data.append([k, v1 == v2, v1, v2])

    # show either not equal or equal one first
    data.sort(key=lambda x: (x[1], x[0]))

    x = PrettyTable()
    x.field_names = ["PropertyName", "IsEqual", config_filename_1, config_filename_2]
    x.align["PropertyName"] = "l"
    for r in data:
        x.add_row(r)

    return x


def main():

    # 1. read contents
    config_filename_1 = sys.argv[1]
    config_filename_2 = sys.argv[2]
    with open(config_filename_1) as f1, open(config_filename_2) as f2:
        raw_content_config_1 = f1.read()
        raw_content_config_2 = f2.read()
        print("====== Config 1 =====")
        print(raw_content_config_1)
        print("====== Config 2 =====")
        print(raw_content_config_2)

        content_config_1 = parse_content(raw_content_config_1)
        content_config_2 = parse_content(raw_content_config_2)

    print(format_data(config_filename_1, config_filename_2, content_config_1, content_config_2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
