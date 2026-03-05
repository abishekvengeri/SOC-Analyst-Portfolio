# False Positive Reduction Tool

**A custom Python tool to filter out SOC alert noise and find real threats.**

## What this project does
Looking at thousands of honeypot logs manually takes too much time and leads to alert fatigue. I built this tool to act as an automated filter. It takes messy raw logs, drops the background internet noise, scores the real threats, and sends an alert straight to my phone.

**The Results:**
* Processed 524,184 raw honeypot events.
* Cut out over 70% of the useless connection noise.
* Turned half a million logs into a simple "Top 10" priority dashboard.

---

## How I built it

### Phase 1: Cleaning the Data
* **The Problem:** Raw Cowrie SSH logs are messy JSON files full of automated connection drops that don't matter.
* **What I did:** I wrote a Python script using the pandas library to read multiple days of logs, organize the data, and drop any event that wasn't a direct attack or login attempt.

### Phase 2: Finding the Attackers
* **The Problem:** Even after filtering, 150,000 alerts is too many to check by hand.
* **What I did:** I grouped the alerts by IP address to see what each attacker was doing. I created an "Aggression Score" to rank them based on how many different usernames and passwords they tried to guess.

### Phase 3: Risk Scoring with Threat Intel
* **The Problem:** Just because an IP is active doesn't mean it is the biggest threat.
* **What I did:** I connected my script to the AbuseIPDB API to check the reputation of each IP. Then, I built a Risk Engine that gives each attacker a score from 0 to 100 based on three things: if they successfully logged in, their global API reputation, and their aggression score.

### Phase 4: Phone Alerts
* **The Problem:** A SOC analyst can't stare at a dashboard 24/7.
* **What I did:** I integrated the Telegram Bot API. Now, if the tool finds a confirmed threat with a Risk Score over 80, it instantly sends a formatted alert directly to my mobile phone.

---

## Tools I Used

* **Language:** Python 3
* **Libraries:** pandas, requests
* **APIs:** AbuseIPDB, Telegram Bot API
* **Security:** Used a .env file and .gitignore to keep my API keys safe and hidden from GitHub.

---

## Screenshots

*(Add your terminal screenshot here showing the 524k to 152k reduction)*

*(Add your Priority Dashboard screenshot here showing the 100% Risk Score threat)*

*(Add your Priority Dashboard screenshot here showing the 100% Risk Score threat)*

---

## How to run the tool

1. **Download the project:**
    git clone https://github.com/abishekvengeri/SOC-Analyst-Portfolio.git
    cd "SOC-Analyst-Portfolio/9-Advance project/False-Positive-Reduction-Tool"

2. **Set up the Python environment:**
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. **Add your API keys:**
    Create a file named .env in the folder and add your keys like this:
    ABUSEIPDB_API_KEY=your_intel_key
    TELEGRAM_BOT_TOKEN=your_bot_token
    TELEGRAM_CHAT_ID=your_chat_id

4. **Run the script:**
    python3 main.py
