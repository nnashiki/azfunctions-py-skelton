import datetime
from logging import DEBUG

import azure.functions as func
from _pytest.logging import LogCaptureFixture
from pydantic import ValidationError

from eventfunc import main


class TestEventFunction:
    def test_first(self):
        event = func.EventGridEvent(
            id="123",
            data={
                "api": "PutBlockList",
                "clientRequestId": "6d79dbfb-0e37-4fc4-981f-442c9ca65760",
                "requestId": "831e1650-001e-001b-66ab-eeb76e000000",
                "eTag": "0x8D4BCC2E4835CD0",
                "contentType": "text/plain",
                "contentLength": 524288,
                "blobType": "BlockBlob",
                "url": "https://my-storage-account.blob.core.windows.net/testcontainer/new-file.txt",
                "sequencer": "00000000000004420000000000028963",
                "storageDiagnostics": {"batchId": "b68529f3-68cd-4744-baa4-3c0498ec19f0"},
            },
            topic="/subscriptions/{subscription-id}/resourceGroups/Storage/providers/Microsoft.Storage/storageAccounts/my-storage-account",
            subject="/blobServices/default/containers/test-container/blobs/new-file.txt",
            event_type="Microsoft.Storage.BlobCreated",
            event_time=datetime.datetime.now(),
            data_version="test",
        )

        result = main(event)
        assert result is None

    def test_validation_error(self, caplog: LogCaptureFixture):
        # ログレベルの設定
        caplog.set_level(DEBUG)

        # 関数を実行
        event = func.EventGridEvent(
            id="123",
            data={
                "clientRequestId": "6d79dbfb-0e37-4fc4-981f-442c9ca65760",
                "requestId": "831e1650-001e-001b-66ab-eeb76e000000",
                "eTag": "0x8D4BCC2E4835CD0",
                "contentType": "text/plain",
                "contentLength": 524288,
                "blobType": "BlockBlob",
                "url": "https://my-storage-account.blob.core.windows.net/testcontainer/new-file.txt",
                "sequencer": "00000000000004420000000000028963",
                "storageDiagnostics": {"batchId": "b68529f3-68cd-4744-baa4-3c0498ec19f0"},
            },
            topic="/subscriptions/{subscription-id}/resourceGroups/Storage/providers/Microsoft.Storage/storageAccounts/my-storage-account",
            subject="/blobServices/default/containers/test-container/blobs/new-file.txt",
            event_type="Microsoft.Storage.BlobCreated",
            event_time=datetime.datetime.now(),
            data_version="test",
        )

        try:
            _ = main(event)
        except Exception as e:
            assert isinstance(e, ValidationError)
            assert (
                "root",
                40,
                "e=ValidationError(model='StorageBlobCreatedEvent', errors=[{'loc': ('data', 'api'), 'msg': 'field required', 'type': 'value_error.missing'}])",
            ) in caplog.record_tuples
