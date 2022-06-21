import json
import logging

import azure.functions as func
from pydantic import BaseModel, ValidationError

from az_evgrid_pydantic_schema import (
    StorageBlobCreatedFull
)


def main(event: func.EventGridEvent):
    logging.info("Azure Event Grid triggered an event")

    # parse event
    try:
        storage_event = StorageBlobCreatedFull(
            id=event.id,
            eventType=event.event_type,
            subject=event.subject,
            data=event.get_json(),
            eventTime=event.event_time,
            dataVersion=event.data_version,
            topic=event.topic,
            metadataVersion=""
        )

        logging.info(F"{storage_event=}")
        logging.info(F"{storage_event.data=}")
    except ValueError as e:
        logging.error("event data をパースできません")
        raise e


    is_success_main_process, message = main_process(storage_event)
    if not is_success_main_process:
        logging.error("main_process が失敗しました")
    return


def main_process(_):
    return True, "success"
