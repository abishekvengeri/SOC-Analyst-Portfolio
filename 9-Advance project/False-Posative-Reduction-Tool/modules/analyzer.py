import pandas as pd

class AlertAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        # Professional fix: low_memory=False handles mixed data types in large CSVs
        self.df = pd.read_csv(file_path, low_memory=False)

    def group_by_attacker(self):
        """
        Groups events by IP to identify persistent actors.
        Calculates an 'Aggression Score' based on username/password variety.
        """
        attacker_stats = self.df.groupby('src_ip').agg({
            'eventid': 'count',                 # Total actions taken
            'username': 'nunique',              # Variety of users targeted
            'password': 'nunique',              # Variety of passwords used
            'session': 'nunique'                # Connection persistence
        }).rename(columns={'eventid': 'total_actions'})
        
        # Calculate a simple 'Aggression Score' 
        # (Total actions * unique users guessed)
        attacker_stats['aggression_score'] = (
            attacker_stats['total_actions'] * attacker_stats['username']
        )
        
        return attacker_stats.sort_values(by='aggression_score', ascending=False)

    def find_successful_breaches(self):
        """
        Filters for attackers who actually bypassed the first layer of defense.
        This represents High-Fidelity alert data.
        """
        # Ensure we only grab rows where login was successful
        success_df = self.df[self.df['eventid'] == 'cowrie.login.success']
        
        # Select relevant columns and drop duplicates to avoid redundant alerts
        return success_df[['timestamp', 'src_ip', 'username', 'password']].drop_duplicates()

    def get_attack_timeline(self, ip_address):
        """
        Portfolio Feature: Get a specific timeline for a high-risk IP.
        Useful for 'deep-dive' analysis in a SOC incident report.
        """
        ip_data = self.df[self.df['src_ip'] == ip_address]
        return ip_data[['timestamp', 'eventid', 'username']].sort_values(by='timestamp')

if __name__ == "__main__":
    # Self-test logic
    try:
        analyzer = AlertAnalyzer("data/processed/cleaned_alerts.csv")
        print("\n[!] Top 5 Most Aggressive Attackers (by Aggression Score):")
        print(analyzer.group_by_attacker().head(5))
    except FileNotFoundError:
        print("[-] Data file not found. Ensure Phase 1 (Ingestion) has run.")
