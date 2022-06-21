import json
from unittest.mock import patch

import azure.functions as func

from azfunc import main


class TestEventFunction:
    def test_first(self):
        req_body = {"param_str": "hoge", "param_int": 1}
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

