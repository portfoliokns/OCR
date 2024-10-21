# このリポジトリについて
このリポジトリはOCRをもとに、画像から文字を抽出するためのリポジトリになります。そのサンプルコードとバッチファイルを用意しています。なおwindows環境で実行するリポジトリになります。

# 準備
## Tesseractのダウンロード & インストール
### ダウンロード
以下のサイトから環境に応じた実行ファイルをダウンロード

https://github.com/UB-Mannheim/tesseract/wiki

ダウンロードした実行ファイルを実行して、インストールする。

"Choose Components"で"Additional script data(download)"と"Additional language data(download)"を開いて、以下の項目にチェックに入れる

"Additional script data(download)"→"Japanese Script", "Japanese vertical script"

"Additional language data(download)"→"Japanese", "Japanese(vertical)"※下側の2つ

### ファイルの書き換え

"ocr.bat"のコードを開いて、"cd C:\ocr-copy.pyがあるパスに変更してください。"を書き換える。ここにはGitHubからクローンした先のパスを書いてください。

### インストール
python,pyocr,pyperclipをインストールしてください。

開発段階では"Python 3.10.6"を使用していました。（バージョンによって互換性があるかもしれません）

```
pip install pyocr
```

```
pip install pyperclip
```

# 使い方
## ocr-pic.py
付属の"test.png"から文字を読み取るソース。実行することで、ターミナル上に読み取った文字が表示されます。

## orc-clip.py
コピーした画像から文字を読み取るソース。あらかじめ読み取りたい画像を範囲選択し、コピーしてください（Win + Shift + S で画像キャプチャ）。その後、実行することで、ターミナル上に読み取った文字が表示されます。

## orc-copy.py
コピーした画像から文字を読み取り、クリップボードに保存するソース。あらかじめ読み取りたい画像を範囲選択し、コピーしてください（Win + Shift + S で画像キャプチャ）。その後、実行することで、ターミナル上に読み取った文字が表示されると同時に、クリップボードに保存されます。ペーストすることができるようになります。

## orc.bat
"orc-copy.py"を実行するバッチファイル。ショートカットキーを設定すれば、即座に文字を読み取る機能を実装することができます。（ショートカットキーへの設定は各種環境で手動で行う必要があります）
