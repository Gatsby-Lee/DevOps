import pyarrow.parquet as pq

from typing import List

from pyathena import connect as pyathena_connect

LOGGER = logging.getLogger(__name__)

def fetch_date_level_data(db_name: str, table_name: str, created_date: str, output_filename: str):

    query = f"""SELECT * FROM {db_name}.{table_name}
WHERE CAST(source_created_date as date) = date('{created_date}')
ORDER BY org_id;
"""

    conn = cursor = None
    try:
        conn = pyathena_connect(region_name="us-west-2", work_group="devlocal-readonly")
        cursor = conn.cursor()
        LOGGER.info("Running query: %s", query)
        cursor.execute(query)

        LOGGER.info("Writing content to %s", output_filename)
        with open(output_filename, "w") as fw:
            for row in r_value:
                lrow = list(row)
                # converting datetime object to timestamp compatiable strint format
                # https://stackoverflow.com/questions/46318714/how-do-i-generate-a-python-timestamp-to-a-particular-format
                lrow[1] = lrow[1].strftime("%Y-%m-%dT%H:%M:%S.%f")
                fw.write("%s\n" % json.dumps(lrow))
    finally:
        cursor and cursor.close()
        conn and conn.close()
