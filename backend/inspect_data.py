import requests
import json

ID = 545361 # Mike Trout
URL = f"https://statsapi.mlb.com/api/v1/people/{ID}?hydrate=stats(group=[hitting,pitching],type=[yearByYear])"

print(f"Fetching data from: {URL}")
res = requests.get(URL)
data = res.json()

stats = data['people'][0]['stats']

print("\n--- STAT GROUPS FOUND ---")
for s in stats:
    print(f"Group: {s['group']['displayName']}, Type: {s['type']['displayName']}, Splits: {len(s.get('splits', []))}")

print("\n--- SAMPLE SPLIT (YEAR BY YEAR) ---")
# Find yearByYear
yby = next((s for s in stats if s['type']['displayName'] == 'yearByYear'), None)
if yby and yby.get('splits'):
    sample = yby['splits'][-1] # Last one (most recent)
    print(json.dumps(sample, indent=2))
else:
    print("No yearByYear splits found.")
