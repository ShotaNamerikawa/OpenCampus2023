# OpenCampus2023
2023年オープンキャンパスのプログラム体験のソースコードを開発、保存するためのレポジトリです。

## 共同でコードを書いてくださる方へ
はじめにこのレポジトリをcloneしてください。Linuxの場合のやり方を載せます。WindowsやMacでもgitがインストールされて入れば同じようにできると思います。

はじめにこのレポジトリのトップページ(Codeのページ)を開き、緑色のCodeのボタンを押すとプルダウンが表示されるのでHTTPもしくはSSHのボタンを押し、このレポジトリのURLをコピーします。
次に
```
git clone "コピーしたURL" 
```
をターミナルから実行しトークン(HTTPの場合)もしくはSSHキーのパスワードを入力してください。そして
```
cd OpenCampus2023
git branch "各々のブランチ名"
git checkout "各々のブランチ名"
mkdir "個人のフォルダ"
```
を実行し、個人のブランチ、個人のフォルダの中でソースコードを作成するようお願い致します。


## 運用方法

### ソースコードの保存方法
個人のディレクトリをこのレポジトリのルートに作ってその下にソースコードを保存してください。他の人のディレクトリ下のファイルは読み込むためだけに使い、編集しないようにしてください。
万が一編集した場合はそのファイルをステージングしてコミットしないようにしてください。

### ブランチの作成について
mainブランチを保護するために直接pushを行えない設定にしています。mainブランチから自分のブランチ(他の人のブランチの名前と重複しないようにしてください)を切って
そのブランチにcommitを行いpushするようにしてください。

### プルリクエストについて
ある程度コードができたら適宜プルリクエストを出して自分のブランチをmainにマージするようにしてください。以下にやり方を説明します。
Codeのページで"Compare and Pull request"のボタンを押すと違うページに移るのでそこのcreate pull requestを押してください。さらに違うページに移るのでそのページの緑色のmergeを押しconfirmを押してください。プルリクエストが承認されます。branchはdeleteしないようにしてください。
