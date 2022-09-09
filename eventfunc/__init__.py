import logging

import azure.functions as func
from az_evgrid_pydantic_schema import StorageBlobCreatedEvent
from pydantic import ValidationError


def main(event: func.EventGridEvent) -> bool:
    logging.info("Azure Event Grid triggered an event")

    # parse event
    try:
        storage_event = StorageBlobCreatedEvent(
            id=event.id,
            eventType=event.event_type,
            subject=event.subject,
            data=event.get_json(),
            eventTime=event.event_time,
            dataVersion=event.data_version,
            topic=event.topic,
            metadataVersion="",
        )

        logging.info(f"{storage_event.data=}")
    except ValidationError as e:
        logging.error(f"{e=}")
        raise e

    is_success_main_process, message = main_process(storage_event)
    if not is_success_main_process:
        logging.error("main_process が失敗しました")
    return True


def main_process(_):
    return True, "success"
