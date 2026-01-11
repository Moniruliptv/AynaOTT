import requests
import json
import re
from collections import defaultdict

M3U_URL = "https://raw.githubusercontent.com/Moniruliptv/AynaOTT/refs/heads/main/Aynaott2.m3u"

PLAYLIST_JSON = "playlist.json"
COUNT_JSON = "count.json"

CATEGORY_ORDER = [
    "Bangla",
    "News",
    "Sports",
    "Channels",
    "documentary",
    "English",
    "Hindi",
    "Indian Bangla",
    "Kids",
    "Latest",
    "movie",
    "music",
    "Religious",
    "Star channels",
    "Urdhu",
    "Weather"
]

def parse_m3u(m3u_text):
    channels = []
    lines = [l.strip() for l in m3u_text.splitlines() if l.strip()]

    for line in lines:
        if line.startswith("#EXTINF"):
            channel = {
                "id": "",
                "title": "",
                "image": "",
                "category": ""
            }

            m_id = re.search(r'tvg-id="([^"]*)"', line)
            m_logo = re.search(r'tvg-logo="([^"]*)"', line)
            m_group = re.search(r'group-title="([^"]*)"', line)

            if m_id:
                channel["id"] = m_id.group(1)
            if m_logo:
                channel["image"] = m_logo.group(1)
            if m_group:
                channel["category"] = m_group.group(1).strip()

            channel["title"] = line.split(",")[-1].strip()
            channels.append(channel)

    return channels


def sort_by_category(channels):
    def index(cat):
        return CATEGORY_ORDER.index(cat) if cat in CATEGORY_ORDER else len(CATEGORY_ORDER)
    return sorted(channels, key=lambda x: index(x["category"]))


def generate_count(channels):
    count = defaultdict(int)

    for ch in channels:
        cat = ch["category"] if ch["category"] else "Unknown"
        count[cat] += 1

    result = {"total": len(channels)}

    # ordered categories
    for cat in CATEGORY_ORDER:
        if cat in count:
            result[cat] = count[cat]

    # unknown / extra categories
    for cat, val in count.items():
        if cat not in CATEGORY_ORDER:
            result[cat] = val

    return result


def main():
    r = requests.get(M3U_URL, timeout=20)
    r.raise_for_status()

    channels = parse_m3u(r.text)
    sorted_channels = sort_by_category(channels)
    count_data = generate_count(channels)

    with open(PLAYLIST_JSON, "w", encoding="utf-8") as f:
        json.dump(sorted_channels, f, indent=4, ensure_ascii=False)

    with open(COUNT_JSON, "w", encoding="utf-8") as f:
        json.dump(count_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Total Channels: {count_data['total']}")
    print("📁 playlist.json + count.json generated successfully")


if __name__ == "__main__":
    main()
