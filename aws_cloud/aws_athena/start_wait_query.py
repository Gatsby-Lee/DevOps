import logging

LOGGER = logging.getLogger(__name__)

def run_query(db_name: str, table_name:str):
    client = boto3.client("athena")

    # run query
    query = f"SELECT count(1) as count FROM {db_name}.{table_name}"
    LOGGER.info("query=%s", query)
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": db_name},
    )
    query_execution_id = response["QueryExecutionId"]

    sleep_time = 5
    # wait until query finish
    while True:
        response = client.get_query_execution(QueryExecutionId=query_execution_id)
        current_query_state = response["QueryExecution"]["Status"]["State"]
        LOGGER.info(
            "State=%s | QueryExecutionId=%s", current_query_state, query_execution_id
        )
        # 'QUEUED'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED'
        current_query_state = response["QueryExecution"]["Status"]["State"]
        if current_query_state not in ["QUEUED", "RUNNING"]:
            break

        LOGGER.info("Current State=%s | sleep %s sec", current_query_state, sleep_time)
        time.sleep(5)

    response = client.get_query_results(
        QueryExecutionId=query_execution_id, MaxResults=1000
    )
    
    return response
