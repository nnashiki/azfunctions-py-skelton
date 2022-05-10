import json
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body: dict = req.get_json()
        logging.debug(req_body)
    except ValueError:
        return func.HttpResponse("Invalid body", status_code=400)

    # ここに validation を入れる

    if "hoge" in req_body:
        result = req_body["hoge"]
    else:
        result = "success"

    is_success_main_process, message = main_process(req_body)

    if is_success_main_process is True:
        res_body = {"message": message}
        return func.HttpResponse(
            json.dumps(res_body),
            status_code=200,
            mimetype="application/json",
        )
    else:
        return func.HttpResponse("process error", status_code=500)


def main_process(_) -> (bool, str):
    return True, "success"
