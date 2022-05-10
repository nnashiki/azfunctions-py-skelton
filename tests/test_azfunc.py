import json
from unittest.mock import patch

import azure.functions as func

from azfunc import main


class TestFunction:
    def test_first(self):
        req_body = {"hoge": "foo"}
        req_headers = {}
        req = func.HttpRequest(
            method="POST",
            body=json.dumps(req_body).encode("utf-8"),
            url="/api/azfunc",
            headers=req_headers,
        )
        resp = main(req)
        assert resp.status_code == 200
        resp_json = json.loads(resp.get_body().decode())
        assert resp_json["message"] == "success"

    def test_second(self):
        req_body = {}
        req_headers = {}
        req = func.HttpRequest(
            method="POST",
            body=json.dumps(req_body).encode("utf-8"),
            url="/api/azfunc",
            headers=req_headers,
        )
        resp = main(req)
        assert resp.status_code == 200
        resp_json = json.loads(resp.get_body().decode())
        assert resp_json["message"] == "success"

    def test_req_body_parse_error(self):
        req_body = {}
        req_headers = {}

        def raise_exception(*args, **kwargs):
            raise ValueError

        with patch("azure.functions.HttpRequest.get_json", new=raise_exception):
            req = func.HttpRequest(
                method="POST",
                body=json.dumps(req_body).encode("utf-8"),
                url="/api/azfunc",
                headers=req_headers,
            )
            resp = main(req)
            assert resp.status_code == 400
            assert resp.get_body().decode() == "can't parse body"

    def test_main_process_error(self):
        req_body = {}
        req_headers = {}

        def main_process_error(*args, **kwargs):
            return False, "Fail"

        with patch("azfunc.main_process", new=main_process_error):
            req = func.HttpRequest(
                method="POST",
                body=json.dumps(req_body).encode("utf-8"),
                url="/api/azfunc",
                headers=req_headers,
            )
            resp = main(req)
            assert resp.status_code == 500
            assert resp.get_body().decode() == "process error"
