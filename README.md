# Tracking_Django

#### 前提
* Dockerがインストールされていること
* Windows
[https://hub.docker.com/editions/community/docker-ce-desktop-windows/](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

> ※インストール中に「WSL2 Linuxカーネルの更新」を求められた場合は下記URL内に記載されているようにLinuxカーネルの更新プログラムをダウンロードしてインストールする。
> 
> [https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-kernel](https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-kernel)

PowerShell上からdockerコマンドおよびdocker-composeコマンドが実行できることを確認する。

```bash
docker --version
docker-compose --version
```

* Mac
* 以下を参照
[https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/)	

* Gitがインストールされていること
* Windows
Git for Windowsをインストールする。（インストール時のオプションはデフォルトのままでよい）
[https://gitforwindows.org/](https://gitforwindows.org/)

* Mac
* 以下を参照
[https://tracpath.com/bootcamp/git-install-to-mac.html](https://tracpath.com/bootcamp/git-install-to-mac.html)	


#### 開発環境構築手順
リポジトリをローカルファイルに保存
  * Zipファイルの場合
  	* Download　Zipを押下
  * コマンドの場合
  	```bash
            git clone https://github.com/kogusanpro/tracking_django.git
	```
	
#### コンテナ起動
リポジトリフォルダ直下まで移動し、以下のコマンドを実行する。
```bash
    docker-compose up -d
```

#### Visual Studio Codeでの開発手順
現状、Dockerコンテナを利用した開発ではVisual Studio Code（[https://code.visualstudio.com/](https://code.visualstudio.com/)）を使用するのが最適である。

ここでは、Visual Studio Code（以下、VSCode）を用いた開発手順例を記載する。

#### VSCode拡張機能のインストール
VSCodeで以下の拡張機能（=プラグイン）をインストールする。

- Japanese Language Pack for Visual Studio Code（[https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)）

    用途：VSCodeの日本語化

- Docker（[https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)）

    用途：主にDockerコンテナの操作で利用

- Remote Containers（[https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)）

    用途：コンテナ上のファイル編集やコマンド実行をVSCode上で行う

#### コンテナ起動
1. VSCodeからリポジトリフォルダ（tracking_django）を開く。
    
1. 以下のいずれかの手順でRemote Containerプラグインを用いてコンテナ内部をVSCode上で開く。
    - VSCodeが起動してしばらくするとVSCode右下に「Folders contains a Dev Container configuration file. ～」というポップアップが表示されるので、ポップアップ内の[Reopen in Container]ボタンを押下
    - VSCode左下にある緑色の「><」のようなボタンを押下し、VSCode上部に表示される選択肢から「Remote-Containers: Reopen in Container」を選択
    - VSCodeで[F1]キーを押下し、上部に表示される検索テキストボックスから「Remote-Containers: Reopen in Container」を検索して選択する

1. しばらくするとVSCodeがコンテナ内部の表示に切り替わる ※初回実施時にはコンテナ作成やVSCodeプラグイン等のダウンロードがあるため少し時間がかかる

#### プログラム実行
VSCode下部にターミナルが表示されていない場合は、メニューの[ターミナル]→[新しいターミナル]を選択するとコンテナのbashが起動する。（bashのため、lsやcat等のLinuxコマンドも実行可能）

アプリケーションを確認する場合、bash上で直接コマンドを実行する。

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

## その他
#### Postgresコンテナへの接続情報
Windows上のPostgresクライアント（MySQL Workbench、HeidiSQLなど）からMySQLコンテナへ接続する際は以下の接続情報を使用する。

|項目|値|
|:---|:---|
|ホスト|localhost または 127.0.0.1|
|ポート|5432|
|ユーザー|root|
|パスワード|password|
|データベース|postgres|

※接続エラーとなる場合はpostgresコンテナが開始しているか確認すること


#### 不要なDockerイメージやコンテナを削除する方法
VSCodeの「Remote Containers」の拡張機能では
- Dockerfileやdocker-compose.ymlを更新した場合
- 上記のDockerイメージを再作成した場合

にDockerイメージを新しく作成している。

このままだと古いDockerイメージで開発端末のデータ量を徐々に圧迫されていくので、定期的にPowerShellで以下のコマンドを実行し不要なイメージやコンテナを削除する。

```bash
docker system prune # 削除するかどうかの確認があるが「y」を入力
```

#### Memo
* トラッキングアプリ情報整理
* 概要
	- フロント画面
		+ ログイン
		+ サインアップ
		+ ログアウト
		+ スケジュール起動
		+ キーワード文字列入力フォーム
		+ 実行ボタン

	- サーバーサイド
		+ 受け取ったキーワード文字列にて検索を行い、クローリング

	* 使用ツール
		* Django(webフレームワーク)
		* Bootstarap(デザイン)
		* firebase(サーバー)
		* Chrome？

	* モジュール
		* schedule
		* matplot

	* 懸念点
		* DjangoとFirebaseの連携方法
		* Djangoのスケジュール実行方法
		* 
