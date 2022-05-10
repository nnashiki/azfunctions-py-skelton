# azfunctions-py-skelton
azure functions Python runner の skelton

## how to develop
- poetry を install する
- `poetry shell` で仮想環境に入る
- `poetry install` で必要なパッケージを install する
- `poetry run task pytest` で unit test を実行する
- `poetry run task fmt` で format を実行する 

## deploy and run
- `poetry export -f requirements.txt --output requirements.txt` を実行して requirements.txt を書き出す
- VSCode から deploy する
- authLevel が function で設定してあるので、deploy された関数を実行するにはクエリパラメータ `code` を付ける必要がある
