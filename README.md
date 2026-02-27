# 🛡️ Sentinel-Duty AI
### *Real-time UK Consumer Duty & Vulnerability Detection Engine*

**Sentinel-Duty AI** is a Fintech MVP designed to help UK financial institutions comply with the **FCA Consumer Duty (2026 Standards)**. It uses AI-driven pattern recognition to identify "Vulnerable Customers" before they fall into financial distress.

## 🚀 Key Features
* **Behavioral Analytics:** Detects "Gambling Spirals" and "Income Shocks".
* **CEO Dashboard:** High-level metrics for compliance officers.
* **FCA-Aligned:** Built specifically for the UK regulatory landscape.
* **Privacy First:** Local SQLite implementation ensuring GDPR compliance.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Database:** SQLite
* **Frontend:** Streamlit
* **Visualization:** Plotly

## 📥 Installation & Setup
1. Clone the repo: `git clone https://github.com/yourusername/sentinel_duty_ai.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Generate mock data: `python src/database.py`
4. Launch Dashboard: `streamlit run src/main.py`