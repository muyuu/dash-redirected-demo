# MPEG-DASH redirect demo manifest

## 用途
- マニフェストがリダイレクトするケース
- セグメントがリダイレクトするケース

上記ケースでの再生確認用のマニフェストを配信するサーバです

## 使い方

### サーバ起動

```sh
$ cp [your certificate] ./cert/server-cert.pem
$ cp [your private key] ./cert/server-key.pem
$ pip install Flask
$ python app.py
```

これで以下ストリームへのアクセスが可能になります。
| URL  | 説明  |
| --- | --- |
| https://{your_domain}:2525/redirect.mpd | マニフェストがリダイレクトするマニフェスト |
| https://{your_domain}:2525/manifest.mpd | セグメントがリダイレクトするマニフェスト |

