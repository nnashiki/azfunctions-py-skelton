# azfunctions-py-skelton
azure functions Python runner の skelton

## how to develop
- poetry を install する
- `poetry shell` で仮想環境に入る
- `poetry install` で必要なパッケージを install する
- `poetry run task test` で unit test を実行する
- `poetry run task fmt` で format を実行する 

## deploy and run
- `poetry export -f requirements.txt --output requirements.txt` を実行して requirements.txt を書き出す
- VSCode から deploy する
- authLevel が function で設定してあるので、deploy された関数を実行するにはクエリパラメータ `code` を付ける必要がある

# HTTP Trigger function (azfunc)に関して
## azure function に deploy して実施したテスト
- body を `` (非json形式)で request する
    - `can't parse body` が返る
- body を `{}` で request する
    - `need any body parameters` が返る
- body を `{"param_str": "hoge"}` で request する
    - `"msg": "field required" を含むエラーが返る`
- body を `{"param_str": "hoge", "param_int": 1}` で request する
    - 200 が返る

# Event Trigger function に関して

ローカルでテストするには、以下のコマンドを実行する

```
curl -X POST -H "Content-Type: application/json" -H "aeg-event-type: Notification" -d '{"topic":"/subscriptions/{subscription-id}/resourceGroups/Storage/providers/Microsoft.Storage/storageAccounts/my-storage-account","subject":"/blobServices/default/containers/test-container/blobs/new-file.txt","eventType":"Microsoft.Storage.BlobCreated","eventTime":"2017-06-26T18:41:00.9584103Z","id":"831e1650-001e-001b-66ab-eeb76e069631","data":{"api":"PutBlockList","clientRequestId":"6d79dbfb-0e37-4fc4-981f-442c9ca65760","requestId":"831e1650-001e-001b-66ab-eeb76e000000","eTag":"0x8D4BCC2E4835CD0","contentType":"text/plain","contentLength":524288,"blobType":"BlockBlob","url":"https://my-storage-account.blob.core.windows.net/testcontainer/new-file.txt","sequencer":"00000000000004420000000000028963","storageDiagnostics":{"batchId":"b68529f3-68cd-4744-baa4-3c0498ec19f0"}},"dataVersion":"","metadataVersion":"1"}'  "http://localhost:7071/runtime/webhooks/eventgrid?functionName=eventfunc"
```

# FastAPI Http Trigger function に関して

以下で call できる

https://<hoge>.azurewebsites.net/api/sample