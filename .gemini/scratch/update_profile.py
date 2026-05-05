import json

with open('src/data/profile.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update Summaries
tr_summary = (
    "Ofansif güvenlik bakış açısını savunma stratejileriyle birleştiren, siber güvenliğin derin teknik alanlarına tutkuyla odaklanmış bir mühendisim. "
    "Özellikle uygulama güvenliği, mobil zararlı yazılım analizi, sıfırdan SOC altyapı kurulumu ve kritik altyapı (SCADA/ICS) güvenliği konularında uzmanlaşmaktayım. "
    "Klasik yöntemlerin ötesine geçerek, yapay zeka destekli yeni nesil analiz araçları geliştirmekte ve 'inşa ederek kırma' felsefesiyle güvenliği kod düzeyinde ele almaktayım. "
    "Tehdit avcılığı ve olay müdahalesi (IR) yeteneklerimle kurumların dijital sınırlarını korurken, modern tehditlere karşı proaktif çözümler üretiyorum."
)

en_summary = (
    "I am a cyber security engineer passionate about the deep technical aspects of offensive security combined with defensive strategies. "
    "I specialize in application security, mobile malware analysis, zero-to-hero SOC infrastructure deployment, and critical infrastructure (SCADA/ICS) security. "
    "Going beyond classical methods, I develop next-generation AI-powered analysis tools and approach security at the code level with a 'build to break' philosophy. "
    "By utilizing threat hunting and Incident Response (IR) methodologies, I secure organizational digital boundaries while providing proactive solutions to an ever-evolving threat landscape."
)

data['tr']['about']['summary'] = tr_summary
data['en']['about']['summary'] = en_summary


# Update Skills
new_skills = [
    "Application Security",
    "Mobile Application Penetration Testing",
    "Android Reverse Engineering",
    "Threat Hunting & Incident Response",
    "Network & Web Penetration Testing",
    "SOC Infrastructure Design & Monitoring",
    "Cloud Security & IAM",
    "Radio Frequency (RF) Communications",
    "Unmanned Aerial Vehicle (UAV) Operations",
    "SCADA/ICS Security",
    "SIEM (Splunk, Wazuh)",
    "IDS/IPS & Firewall (Fortinet)",
    "Switching & Routing",
    "Docker & Containerization",
    "LLM Fine Tuning & AI",
    "Image Processing & Computer Vision",
    "Python & Go & C#"
]

data['tr']['skills'] = new_skills
data['en']['skills'] = new_skills

with open('src/data/profile.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Profile updated with skills and summary.")
