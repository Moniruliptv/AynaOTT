import requests

URL = "http://doponsapi.murgifarm.xyz/v2/playlist.m3u"
OUTPUT = "playlist.m3u"

r = requests.get(URL, stream=True)
r.raise_for_status()

with open(OUTPUT, "wb") as f:
    for chunk in r.iter_content(8192):
        if chunk:
            f.write(chunk)

print("M3U saved:", OUTPUT)
