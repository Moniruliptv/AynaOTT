import requests

SOURCE_URL = "https://akashgo.noobmaster.xyz/?api=iptv_m3u"

HEADERS = {
    "User-Agent": "okhttp/4.12.0",
    "X-Requested-With": "com.blaze.sportzfy",
    "Accept-Encoding": "gzip",
    "Referer": "https://akashgo.noobmaster.xyz/"
}

print("Fetching playlist...")

r = requests.get(SOURCE_URL, headers=HEADERS, timeout=20)

if r.status_code == 200:
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("Playlist updated")
else:
    print("Failed:", r.status_code)
