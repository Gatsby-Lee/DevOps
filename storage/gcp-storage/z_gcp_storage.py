"""
:author: Gatsby Lee
:since: 2019-05-08
"""
import argparse

from google.cloud import storage

from pylib.zcomp import get_gzipped_content

DEFAULT_CONTENT_TYPE = 'text/plain'


class GCPStorage(object):
    """
    @note: https://googleapis.github.io/google-cloud-python/latest/storage/blobs.html
    """

    def __init__(self, bucket_name):
        self._client = storage.Client()
        self.bucket = self._client.bucket(bucket_name)

    def store(self, content, object_key: str,
              content_type: str = DEFAULT_CONTENT_TYPE,
              gzip_compressed: str = False):
        blob = self.bucket.blob(object_key)
        if gzip_compressed:
            blob.content_encoding = 'gzip'
        blob.upload_from_string(
            content,
            content_type='text/plain')


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--content', required=True)
    parser.add_argument('--object-key', required=True)
    parser.add_argument('--gzip')
    return parser.parse_args()


def cli_main():

    args = _parse_args()
    s = GCPStorage(args.bucket)
    gzip_compressed = args.gzip
    content = args.content
    if gzip_compressed:
        content = get_gzipped_content(content.encode())
    s.store(content, args.object_key, gzip_compressed=True)
