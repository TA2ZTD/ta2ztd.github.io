import json

with open('src/data/profile.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove from TR
data['tr']['awards'] = [award for award in data['tr']['awards'] if "Devlet Teşvikleri" not in award.get('title', '')]

# Remove from EN
data['en']['awards'] = [award for award in data['en']['awards'] if "State Incentives" not in award.get('title', '')]

with open('src/data/profile.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Removed State Incentives correctly.")
