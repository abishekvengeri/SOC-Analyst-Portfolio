import requests

class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def send_alert(self, ip, score, actions, users_targeted, abuse_score):
        """Sends a formatted Markdown alert to the Telegram chat."""
        # We use a threshold check in main.py, so if this triggers, it's critical.
        message = (
            f"🚨 *CRITICAL THREAT DETECTED* 🚨\n\n"
            f"**IP Address:** `{ip}`\n"
            f"**Priority Score:** {score}/100\n"
            f"**Total Actions:** {actions}\n"
            f"**Users Targeted:** {users_targeted}\n"
            f"**AbuseIPDB Score:** {abuse_score}\n\n"
            f"⚠️ *Action Required: Investigate immediately.*"
        )
        
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        try:
            response = requests.post(self.base_url, data=payload)
            if response.status_code == 200:
                print(f"[+] 📱 Telegram alert sent successfully for IP: {ip}")
            else:
                print(f"[-] 📱 Failed to send Telegram alert. HTTP Status: {response.status_code}")
        except Exception as e:
            print(f"[!] 📱 Notification error: {e}")
