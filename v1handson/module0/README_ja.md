# モジュール0 - Helloworld

## 1. Function Appの作成 (まだ作成していない場合のみ)

* [Create a first Python Function in the Azure portal](https://github.com/yokawasa/azure-functions-python-samples/blob/master/docs/create-function-app-in-azure-portal.md)をベースにAzureポータルで作成

## 2. ソースコードをGithubよりダウンロード
レポジトリ: https://github.com/yokawasa/azure-functions-python-samples

```
git clone https://github.com/yokawasa/azure-functions-python-samples.git
```
もしくはレポジトリからZIPで[ダウンロード](https://github.com/yokawasa/azure-functions-python-samples/archive/master.zip)

モジュール０のマテリアル配置場所: azure-functions-python-samples/handson/module0配下

## 3. Functionのデプロイ

Azureポータルまたはコマンドでデプロイ

* Azureポータルの場合
手順については[こちら](../../docs/create-function-app-in-azure-portal.md)を参照ください

* コマンドの場合 (ここではgit)
手順については[こちら](../../docs/local-git-deployment_ja.md)を参照ください

## 4. Functionのテスト

[こちら](../../docs/create-function-app-in-azure-portal.md#test-the-function)と同様の方法で動作確認

余裕がある場合はソースコードのdump部分のコメントを外して、再デプロイして実行してみてください。Pythonランタイムのバージョンや環境変数が全て出力されます.

```
import os
import platform
import sys
import json

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write("hello world from "+postreqdata['name'])
response.close()

### dump
#print("Python Version = '{0}'".format(platform.python_version()))
#print(sys.version_info)
#for e in os.environ:
#    print ("{}->{}".format(e, os.environ[e]))
```

