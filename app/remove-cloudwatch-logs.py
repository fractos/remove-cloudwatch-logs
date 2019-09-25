import boto3
import datetime
import logging
import logzero
from logzero import logger
import settings

def main():
    client = boto3.client("logs")

    paginator = client.get_paginator("describe_log_streams")

    response_iterator = paginator.paginate(
        logGroupName=settings.LOG_GROUP_NAME,
        logStreamNamePrefix=settings.LOG_STREAM_NAME_PREFIX,
        orderBy="LogStreamName",
        descending=True,
        PaginationConfig={
            "MaxItems": 5000,
            "PageSize": 50
        }
    )

    for page in response_iterator:
        logger.info(f"page started")
        for logstream in page["logStreams"]:
            # logger.info(logstream["logStreamName"])
            if len(settings.KEEP) > 0 and logstream["logStreamName"] == settings.KEEP:
                logger.info(f"keeping {settings.KEEP}")
            elif len(settings.AFTER) > 0 and logstream_newer_than(logstream, settings.AFTER):
                logger.info(f'removing {logstream["logStreamName"]}')
                if not settings.DRY_RUN:
                    client.delete_log_stream(
                        logGroupName=settings.LOG_GROUP_NAME,
                        logStreamName=logstream["logStreamName"]
                    )
            else:
                logger.info(f'skipping {logstream["logStreamName"]}')


def logstream_newer_than(logstream, after):
    epoch = datetime.datetime.utcfromtimestamp(0)

    after_time_obj = datetime.datetime.strptime(after, "%Y-%m-%d %H:%M:%S")

    after_time_epoch_ms = (after_time_obj - epoch).total_seconds() * 1000.0

    logstream_epoch_ms = int(logstream["lastEventTimestamp"])

    return logstream_epoch_ms > after_time_epoch_ms


if __name__ == "__main__":
    if settings.DEBUG:
        logzero.loglevel(logging.DEBUG)
    else:
        logzero.loglevel(logging.INFO)

    main()
