import json

with open('src/data/profile.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Update social links
data['social']['github'] = "https://github.com/ta2ztd"
data['social']['linkedin'] = "https://www.linkedin.com/in/ta2ztd/"
data['social']['huggingface'] = "https://huggingface.co/TA2ZTD"
data['social']['medium'] = "https://medium.com/@ta2ztd"

# 2. Update role for CBERNET
for item in data['tr']['experience']:
    if item['id'] == 1:
        item['role'] = "Cyber Security Engineer - SOC Team Lead"
for item in data['en']['experience']:
    if item['id'] == 1:
        item['role'] = "Cyber Security Engineer - SOC Team Lead"

# 3. Add to technical skills (skills list)
new_skills = [
    "Splunk Core Certified User (SPLK-1001)",
    "Certified Threat Hunting Professional - eCTHPv2",
    "Mobile Application Penetration Tester - eMAPT",
    "INE Certified Junior Penetration Tester - eJPTv2",
    "INE Certified Cloud Associate - ICCA",
    "Certified Android Penetration Tester - CAPT",
    "UAV-1 Amateur / Sportive Pilot License",
    "Amateur Radio Operator License - Class A"
]

# Preserve other skills
def update_skills(skills):
    filtered = [s for s in skills if s not in [
        "eMAPT (Mobile PenTest)", 
        "eCTHPv2 (Threat Hunting)", 
        "eJPT (Junior PenTest)", 
        "ICCA (Cloud Associate)"
    ]]
    return new_skills + filtered

data['tr']['skills'] = update_skills(data['tr']['skills'])
data['en']['skills'] = update_skills(data['en']['skills'])

# 4. Add Awards/Achievements
tr_award = {
    "title": "CVE-2026-6001 Zafiyet Tespiti",
    "organization": "Ulusal Siber Olaylara Müdahale Merkezi (USOM)",
    "date": "2026",
    "description": "Türkiye genelinde 50'den fazla üniversitede aktif olarak kullanılan bir akademik proje süreçleri yönetim sisteminde kritik bir güvenlik zafiyeti tespit ettim. Yaptığım bildirim neticesinde, söz konusu bulgu USOM tarafından değerlendirilerek CVE-2026-6001 kodu ile kayıt altına alınmıştır."
}
en_award = {
    "title": "CVE-2026-6001 Vulnerability Discovery",
    "organization": "National Cyber Incident Response Center (USOM)",
    "date": "2026",
    "description": "I discovered a critical security vulnerability in an academic project process management system actively used in more than 50 universities across Turkey. As a result of my report, the finding was evaluated by USOM and registered with the CVE-2026-6001 code."
}
data['tr']['awards'].insert(0, tr_award)
data['en']['awards'].insert(0, en_award)

# 5. Add News
new_news_tr = [
    {
        "id": 100,
        "date": "Blog",
        "title": "Splunk Core Certified User (SPLK-1001) Sınav Deneyimim",
        "content": "Splunk Core Certified User sınavına hazırlık sürecim ve sınav deneyimim.",
        "link": "https://ta2ztd.medium.com/splunk-core-certified-user-splk-1001-s%C4%B1nav-deneyimim-5edd8e5e2a78"
    },
    {
        "id": 101,
        "date": "Blog",
        "title": "DevSecOps Yolculuğu Bölüm 1: Sıfırdan Otonom Bir Pipeline İnşası",
        "content": "Sıfırdan otonom bir DevSecOps pipeline mimarisi oluşturma rehberi.",
        "link": "https://ta2ztd.medium.com/devsecops-yolculu%C4%9Fu-b%C3%B6l%C3%BCm-1-s%C4%B1f%C4%B1rdan-otonom-bir-pipeline-i%CC%87n%C5%9Fas%C4%B1-3d837fb832b1"
    },
    {
        "id": 102,
        "date": "Blog",
        "title": "Eski Bir Laptop ile Kendi Güvenli Lab Ortamımı Kurdum: Tor Router, Nextcloud NAS ve Zero Trust Mimari #HomeLab2",
        "content": "HomeLab serisi: Eski bilgisayarları değerlendirerek güvenli bir ağ ortamı inşa etmek.",
        "link": "https://ta2ztd.medium.com/eski-bir-laptop-ile-kendi-g%C3%BCvenli-lab-ortam%C4%B1m%C4%B1-kurdum-tor-router-nextcloud-nas-ve-zero-trust-a6b70a9e21f7"
    },
    {
        "id": 103,
        "date": "Blog",
        "title": "AI Çağına Hazırlık: Wazuh, OPNsense ve Proxmox ile Güvenli Bir Dijital Kale İnşa Etmek!",
        "content": "Yapay zeka çağında açık kaynaklı araçlarla (Wazuh, OPNsense, Proxmox) dijital kale inşası.",
        "link": "https://ta2ztd.medium.com/ai-%C3%A7a%C4%9F%C4%B1na-haz%C4%B1rl%C4%B1k-wazuh-opnsense-ve-proxmox-ile-g%C3%BCvenli-bir-dijital-kale-i%CC%87n%C5%9Fa-etmek-afc6e16113dd"
    }
]

new_news_en = [
    {
        "id": 100,
        "date": "Blog",
        "title": "My Splunk Core Certified User (SPLK-1001) Exam Experience",
        "content": "My preparation process and experience with the Splunk Core Certified User exam.",
        "link": "https://ta2ztd.medium.com/splunk-core-certified-user-splk-1001-s%C4%B1nav-deneyimim-5edd8e5e2a78"
    },
    {
        "id": 101,
        "date": "Blog",
        "title": "DevSecOps Journey Part 1: Building an Autonomous Pipeline from Scratch",
        "content": "A guide to building an autonomous DevSecOps pipeline architecture from scratch.",
        "link": "https://ta2ztd.medium.com/devsecops-yolculu%C4%9Fu-b%C3%B6l%C3%BCm-1-s%C4%B1f%C4%B1rdan-otonom-bir-pipeline-i%CC%87n%C5%9Fas%C4%B1-3d837fb832b1"
    },
    {
        "id": 102,
        "date": "Blog",
        "title": "Building My Secure Lab Environment with an Old Laptop: Tor Router, Nextcloud NAS, and Zero Trust Architecture #HomeLab2",
        "content": "HomeLab series: Building a secure network environment by repurposing old computers.",
        "link": "https://ta2ztd.medium.com/eski-bir-laptop-ile-kendi-g%C3%BCvenli-lab-ortam%C4%B1m%C4%B1-kurdum-tor-router-nextcloud-nas-ve-zero-trust-a6b70a9e21f7"
    },
    {
        "id": 103,
        "date": "Blog",
        "title": "Preparing for the AI Era: Building a Secure Digital Fortress with Wazuh, OPNsense, and Proxmox!",
        "content": "Building a digital fortress with open-source tools (Wazuh, OPNsense, Proxmox) in the AI era.",
        "link": "https://ta2ztd.medium.com/ai-%C3%A7a%C4%9F%C4%B1na-haz%C4%B1rl%C4%B1k-wazuh-opnsense-ve-proxmox-ile-g%C3%BCvenli-bir-dijital-kale-i%CC%87n%C5%9Fa-etmek-afc6e16113dd"
    }
]

data['tr']['news'] = new_news_tr + data['tr']['news']
data['en']['news'] = new_news_en + data['en']['news']

for i, item in enumerate(data['tr']['news']):
    item['id'] = i + 1
for i, item in enumerate(data['en']['news']):
    item['id'] = i + 1

with open('src/data/profile.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Profile patched successfully.")
