import requests

url = "https://cloudtvplaylist.noobmaster.xyz"
params = {"download": "m3u_playlist"}
headers = {
    "User-Agent": "okhttp/4.12.1",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

r = requests.get(url, params=params, headers=headers)
open("playlist.m3u", "w", encoding="utf-8").write(r.text)
print("DONE")
