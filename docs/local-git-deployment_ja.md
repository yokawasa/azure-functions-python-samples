# [Deprecated] Local Git Deployment to Azure Functions (1.X Function runtime)

**IMPORTANT - Please consider to use 2.X Python funciton as Python function in Azure function 1.X is experimental and new feature investments won't be added to 1.X Python function**

## 1. Step 1: ローカルレポジトリの作成
$ git init
```
$ cd LOCAL_GIT_REPO_DIR
$ git init
    Initialized empty Git repository in /LOCAL_GIT_REPO_DIR/.git/
```

## 2: ローカルレポジトリにソースコードをコミット
"mypyfunc"という名前のfunctionを作成する。ローカルレポジトリルート配下に"mypyfunc"ディレクトリを作成して、その配下にrun.py、 function.json、その他関連ファイルを配置して全てのファイルをコミットする

```
$ cd LOCAL_GIT_REPO_DIR
$ find mypyfunc
$ mypyfunc
$ mypyfunc/function.json
$ mypyfunc/run.py
$ git add mypyfunc
$ git commit -m "Added mypyfunc"
```

## 3: App Service アプリのリポジトリを有効にする
[手順 3: App Service アプリのリポジトリを有効にする](https://docs.microsoft.com/ja-jp/azure/app-service/app-service-deploy-local-git#span-data-ttu-idd68c5-131a-namestep3a手順-3-app-service-アプリのリポジトリを有効にするspanspan-classsxs-lookupspan-data-stu-idd68c5-131a-namestep3astep-3-enable-the-app-service-app-repositoryspanspan)を参考にFunction Appに対して Git リポジトリを有効にする


## 4: プロジェクトをデプロイする

ポータルのFunction Appの[設定]、[プロパティ] の順にクリックし、[Git URL (Git の URL)] を確認
```
 Git URL例: https://yoichika@yoichikademo27.scm.azurewebsites.net:443/yoichikademo27.git
```

Function AppのGitレポジトリに対して'azure'という名前の参照を作成

```
$ cd LOCAL_GIT_REPO_DIR
$ git remote add azure https://yoichika@yoichikademo27.scm.azurewebsites.net:443/yoichikademo27.git
```

ローカルのコンテンツをFunction Appにプッシュ. この時、初回であれば３のステップで設定・取得したデプロイ資格情報の入力を求められる
```
git push azure master
Password for 'https://yoichika@yoichikademo27.scm.azurewebsites.net:443':
```

以下実行例
```
$  git push azure master
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 389 bytes | 389.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Updating branch 'master'.
remote: Updating submodules.
remote: Preparing deployment for commit id 'c0f99c5a43'.
remote: Generating deployment script.
remote: Running deployment command...
remote: Handling function App deployment.
remote: Not using funcpack because SCM_USE_FUNCPACK is not set to 1
remote: Installing function extensions from nuget
remote: KuduSync.NET from: 'D:\home\site\repository' to: 'D:\home\site\wwwroot'
remote: Copying file: 'mypyfunc\function.json'
remote: Copying file: 'mypyfunc\run.py'
remote: Restoring npm packages in "D:\home\site\wwwroot"
remote: Finished successfully.
remote: Running post deployment command(s)...
remote: Syncing 2 function triggers with payload size 228 bytes successful.
remote: Deployment successful.
To https://yoichikademo27.scm.azurewebsites.net:443/yoichikademo27.git
   902abf2..c0f99c5  master -> master
```
注意: 一旦これでリリースするとPortalでは編集できなくなります


# LINKS
* https://docs.microsoft.com/ja-jp/azure/app-service/app-service-deploy-local-git
