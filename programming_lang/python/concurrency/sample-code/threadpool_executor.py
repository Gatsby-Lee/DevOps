import concurrent.futures

LOGGER = logging.getLogger(__name__)

QUERY = "select count(*) as count from abc where c=123"
TARGETS = [
    "catalog_1",
    "catalog_2",
    "catalog_3",
]

def get_result(target, query):
  pass

def main():
    collected_stats = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_coll_name = {}
        for target in TARGETS:
            query = QUERY % target
            f = executor.submit(
                get_result,
                target,
                query,
            )
            future_to_coll_name[f] = target

        # @note: it's ok to pass the dict format value to `as_completed`. It will build a set with the keys, futures.
        for future in concurrent.futures.as_completed(future_to_coll_name):
            target = future_to_coll_name[future]
            try:
                r, spent_time = future.result()
                collected_stats[target] = (r, spent_time)
            except Exception as e:
                collected_stats[target] = (None, None)
                LOGGER.exception(e)
