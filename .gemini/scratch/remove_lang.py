import json

with open('src/data/profile.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for lang in ['tr', 'en']:
    skills = data[lang]['skills']
    
    if "Python & Go & C#" in skills:
        skills.remove("Python & Go & C#")
        
    for i, skill in enumerate(skills):
        if "IDS/IPS & Firewall (Fortinet)" in skill:
            skills[i] = "IDS/IPS & Firewall (Fortinet, Snort)"

    data[lang]['skills'] = skills

with open('src/data/profile.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Profile updated successfully.")
