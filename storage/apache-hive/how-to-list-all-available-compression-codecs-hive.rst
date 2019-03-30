How to List all available compression codecs hive
=================================================


.. code-block:: bash

  #  List of Available Compression Codecs in Hive
  hive> set io.compression.codecs;
  io.compression.codecs=
    org.apache.hadoop.io.compress.DefaultCodec,
    org.apache.hadoop.io.compress.GzipCodec,
    org.apache.hadoop.io.compress.BZip2Codec,
    org.apache.hadoop.io.compress.DeflateCodec,
    org.apache.hadoop.io.compress.SnappyCodec,
    com.hadoop.compression.lzo.LzopCodec
