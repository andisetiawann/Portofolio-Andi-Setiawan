from django.shortcuts import render


def home(request):
    """Homepage dengan 3 project preview"""
    projects = [
        {
            "title": "Network Automation — Ansible & NAPALM",
            "tech": "Python · Ansible · NAPALM",
            "desc": "Playbooks untuk konfigurasi VLAN, backup config, dan pengujian konektivitas otomatis pada perangkat switch/router.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann"
        },
        {
            "title": "IoT Gas Sensor Dashboard",
            "tech": "ESP32 · MQTT · Flask",
            "desc": "Prototype sensor gas mengirim data ke Mosquitto; dashboard realtime dengan Flask & Chart.js.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann"
        },
        {
            "title": "Wine Quality Classifier",
            "tech": "Python · scikit-learn",
            "desc": "Decision tree classifier pada dataset Wine Quality (UCI) lengkap dengan notebook evaluasi dan pipeline preprocessing.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann"
        },
    ]
    return render(request, 'main/index.html', {"projects": projects})


def about(request):
    """Halaman About"""
    return render(request, 'main/about.html')


def projects(request):
    """Halaman Projects dengan 8 projects lengkap"""
    all_projects = [
        {
            "title": "Sistem Monitoring Jamur dengan ML",
            "tech": "ESP32 · DHT22 · Machine Learning · IoT",
            "desc": "Website sistem monitoring pertumbuhan jamur menggunakan sensor DHT22 dengan integrasi model machine learning untuk prediksi perkembangan optimal.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann",
            "category": "iot"
        },
        {
            "title": "Sistem Monitoring Sungai Rajabasa",
            "tech": "Backend · Frontend · IoT · Monitoring",
            "desc": "Full-stack development sistem monitoring kualitas dan level air sungai di Bandar Lampung Rajabasa dengan real-time data visualization.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann",
            "category": "iot"
        },
        {
            "title": "IoT Gas Sensor Dashboard",
            "tech": "ESP32 · MQTT · Flask · Chart.js",
            "desc": "Prototype sensor gas mengirim data ke Mosquitto broker dengan dashboard real-time menggunakan Flask dan Chart.js untuk visualisasi data.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann",
            "category": "iot"
        },
        {
            "title": "Google Cloud Arcade Facilitator 2025",
            "tech": "Google Cloud · Facilitator · Training",
            "desc": "Fasilitator resmi Google Cloud Arcade 2025, membantu peserta menguasai Google Cloud Platform melalui hands-on labs dan skill badges.",
            "repo": "https://www.linkedin.com/in/andi-setiawan-a67b05280/",
            "doc": "https://www.linkedin.com/in/andi-setiawan-a67b05280/",
            "category": "cloud"
        },
        {
            "title": "Todo List Management System",
            "tech": "Django · Python · Web App",
            "desc": "Website manajemen tugas dengan fitur CRUD lengkap, user authentication, dan kategori task untuk produktivitas yang lebih baik.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann",
            "category": "web"
        },
        {
            "title": "Pemateri Bootcamp SMKN4 Bandar Lampung",
            "tech": "OSPF · BGP · Switching · Networking",
            "desc": "Instruktur bootcamp jaringan komputer selama 4 hari, mengajar OSPF, BGP, switching, dan konfigurasi routing untuk siswa SMK Negeri 4 Bandar Lampung.",
            "repo": "https://www.youtube.com/@AndiSetiawan-wh9je",
            "doc": "https://www.youtube.com/@AndiSetiawan-wh9je",
            "category": "teaching"
        },
        {
            "title": "Cloud Infrastructure Automation",
            "tech": "Kubernetes · Docker · Terraform · CI/CD",
            "desc": "Infrastructure as Code menggunakan Terraform, containerization dengan Docker, dan orchestration dengan Kubernetes untuk deployment otomatis.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann",
            "category": "cloud"
        },
        {
            "title": "Network Security Configuration Lab",
            "tech": "Mikrotik · Cisco · VLAN · Security",
            "desc": "Implementasi keamanan jaringan menggunakan Mikrotik dan Cisco, konfigurasi VLAN, ACL, dan firewall rules untuk enterprise network.",
            "repo": "https://github.com/andisetiawann",
            "doc": "https://github.com/andisetiawann",
            "category": "teaching"
        },
    ]
    
    return render(request, 'main/projects.html', {"projects": all_projects})


def certifications(request):
    """Halaman Certifications - TAMBAHKAN INI"""
    return render(request, 'main/certifications.html')


def contact(request):
    """Halaman Contact"""
    return render(request, 'main/contact.html')