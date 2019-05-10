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

    def store(self, content, object_key: str,
              content_type: str,
              content_encoding: str):
        blob = self.bucket.blob(object_key)
        blob.content_encoding = content_encoding
        blob.upload_from_string(content,
                                content_type=content_type)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--content', required=True)
    parser.add_argument('--object-key', required=True)
    parser.add_argument('--content-type', required=True)
    parser.add_argument('--content-encoding', required=True)
    return parser.parse_args()


def cli_main():
    args = _parse_args()
    s = GCPStorage(args.bucket)
    content = args.content
    s.store(content, args.object_key, args.content_type, args.content_encoding)
