# ⚡ Advanced IP Logger

[![Python Version](https://shields.io)](https://python.org)
[![Maintenance](https://shields.io)](https://github.com)

A highly efficient, asynchronous Python utility designed to collect comprehensive user analytics, system metadata, and network geolocation data, forwarding payloads directly to a designated Discord webhook.

---

## 🚀 Key Features

* **Deep Telemetry Parsing**: Extracts over 70 unique user and system data points.
* **Network Geolocation**: Resolves ISP, country, city, coordinates, timezone, and AS details via `ip-api.com`.
* **User-Agent Fingerprinting**: Pinpoints browser engines, hardware device types, OS versions, and adblock status.
* **System Hardware Metrics**: Captures CPU architecture, machine release details, platform parameters, and hostnames.
* **Instant Exfiltration**: Securely bundles and streams data payloads directly to your Discord Webhook channel.

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ and the required dependencies installed:
```bash
pip install requests
```

### 2. Configuration
Open `logger.py` and replace the placeholder variable with your actual Discord Webhook URL:
```python
# Open logger.py and update your endpoint:
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"
```

### 3. Execution
Run the script locally or deploy it to your server environments:
```bash
python logger.py
```

---

## 📊 Telemetry Data Breakdown



| Data Layer | Metrics Collected |
| :--- | :--- |
| **🌐 Network** | IP Address, ISP Provider, Autonomous System (AS) Number, AS Name |
| **📍 Geolocation** | Country, Country Code, Region, City, Zip Code, Latitude, Longitude, Timezone |
| **💻 System** | OS Name, OS Version, Platform, Hardware Architecture, Processor Model, Node Name |
| **📱 Client Environment**| Browser Brand, Version String, Device Type, Mobile/PC Status, Adblock Flag |

---

## ⚠️ Disclaimer

This tool is created strictly for educational purposes, authorized security testing, and internal telemetry tracking. Unauthorized deployment targeting non-consenting users is strictly prohibited.
