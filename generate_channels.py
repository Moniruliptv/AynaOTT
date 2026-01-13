import requests
from collections import defaultdict

# ============== CONFIG ==============
RAW_URL = "https://raw.githubusercontent.com/sm-monirulislam/AynaOTT-auto-update-playlist/refs/heads/main/AynaOTT.json"
OUTPUT_FILE = "channels.html"
# ====================================

res = requests.get(RAW_URL, timeout=15)
data = res.json()

# category wise group
categories = defaultdict(list)
for ch in data:
    categories[ch.get("category", "Others")].append(ch)

html = []

cat_index = 0
for cat_name, channels in categories.items():
    html.append(f'<!-- {cat_name.upper()} -->')
    html.append(f'<div id="cat_{cat_index}" class="channel-grid">')

    for ch in channels:
        cid = ch.get("id")
        logo = ch.get("logo")

        html.append(f'''
  <div class="channel-card item-box" onclick="loadChannel('{cid}',this)">
    <div class="inner-card">
      <img src="{logo}">
    </div>
  </div>
''')

    html.append('</div>\n')
    cat_index += 1

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print("✅ HTML Generated:", OUTPUT_FILE)
print("📂 Total Categories:", len(categories))
print("📺 Total Channels:", len(data))
