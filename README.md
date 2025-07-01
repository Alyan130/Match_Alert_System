# 🏏 Match Alert System - WhatsApp Cricket Notifications

A Python project that sends real-time **WhatsApp alerts** when a **new cricket match starts** using the **Cricket API** and **Twilio API**.

---

## 🚀 Features

- 🔔 Get instant WhatsApp alerts when a match goes live
- 📲 Uses Twilio WhatsApp messaging
- 🏏 Fetches live match data from a Cricket API
- ⏲️ Runs on a scheduled interval (e.g., every 5 minutes)
- 🧪 Simple and easy to configure

---

## 🛠️ Tech Stack

- **Python**
- **Twilio API** – for WhatsApp messages
- **Cricket API** – to fetch match data
- **time** – to poll API , to check match start or not

---

## 📦 Installation

### 1. Clone the Repository
- git clone https://github.com/Alyan130/Match_Alert_System.git
- cd match-alert-system

### 2. Install dependancies
uv pip install

### 3. Setup Envoirnment variables
- TWILIO_ACCOUNT_SID=your_twilio_account_sid
- TWILIO_AUTH_TOKEN=your_twilio_auth_token
- TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
- CRICKET_API_KEY=your_cricket_api_key
