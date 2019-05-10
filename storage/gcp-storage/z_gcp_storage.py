"""
:author: Gatsby Lee
:since: 2019-05-08
"""
import argparse

from google.cloud import storage


class GCPStorage(object):
    """
    @note: https://googleapis.github.io/google-cloud-python/latest/storage/blobs.html
    """

    def __init__(self, bucket_name):
        self._client = storage.Client()
        self.bucket = self._client.bucket(bucket_name)

    def is_exist(self, object_key: str):
        return self.bucket.blob(object_key).exists()

    def store_str(self, content, object_key: str,
                  content_type: str,
                  content_encoding: str):
        blob = self.bucket.blob(object_key)
        blob.content_encoding = content_encoding
        blob.upload_from_string(content,
                                content_type=content_type)

    def fetch_str(self, object_key):
        blob = self.bucket.blob(object_key)
        return blob.download_as_string()


def _parse_args():
    parser = argparse.ArgumentParser()

    cmd_parser = parser.add_subparsers(dest='cmd', required=True)
    store_str_parser = cmd_parser.add_parser('store-str')
    store_str_parser.add_argument('--bucket', required=True)
    store_str_parser.add_argument('--content', required=True)
    store_str_parser.add_argument('--object-key', required=True)
    store_str_parser.add_argument('--content-type', required=True)
    store_str_parser.add_argument('--content-encoding', required=True)
    fetch_str_parser = cmd_parser.add_parser('fetch-str')
    fetch_str_parser.add_argument('--bucket', required=True)
    fetch_str_parser.add_argument('--object-key', required=True)
    return parser.parse_args()


def cli_main():
    args = _parse_args()
    s = GCPStorage(args.bucket)
    if args.cmd == 'store-str':
        content = args.content
        s.store_str(content, args.object_key, args.content_type, args.content_encoding)
    elif args.cmd == 'fetch-str':
        r = s.fetch_str(args.object_key)
        print(r)


if __name__ == '__main__':
    cli_main()
