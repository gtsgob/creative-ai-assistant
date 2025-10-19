import json, urllib.request

# Replace with your real Solvay raw file URL:
# Go to Solvay repo -> open data/metrics/intent_manifest.json -> click "Raw" -> copy the URL
SOLVAY_RAW_URL = "PASTE_THE_RAW_URL_HERE"

with urllib.request.urlopen(SOLVAY_RAW_URL, timeout=10) as r:
    data = json.load(r)

# Very simple effect: print a line your assistant can use
mood = data.get("emotional_state", "Neutral")
mode = data.get("output_mode", "Plain")
print(f"[Solvay Bridge] mood={mood} mode={mode} deltaH={data.get('deltaH')} LSSE={data.get('LSSE')}")
