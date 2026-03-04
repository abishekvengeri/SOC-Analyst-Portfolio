import pandas as pd
import json
import os

class CowrieIngestor:
    def __init__(self, raw_dir, processed_dir):
        self.raw_dir = raw_dir
        self.processed_dir = processed_dir

    def load_all_logs(self):
        all_events = []
        # UPDATED: This now looks for ANY file in the folder, not just .json
        files = [f for f in os.listdir(self.raw_dir) if os.path.isfile(os.path.join(self.raw_dir, f))]
        
        if not files:
            print(f"[-] No files found in {self.raw_dir}")
            return pd.DataFrame()

        for file in files:
            # Skip hidden files or the venv folder if it accidentally got moved
            if file.startswith('.'): continue
            
            print(f"[*] Ingesting {file}...")
            try:
                with open(os.path.join(self.raw_dir, file), 'r') as f:
                    for line in f:
                        try:
                            all_events.append(json.loads(line))
                        except:
                            continue
            except Exception as e:
                print(f"[!] Error reading {file}: {e}")
        
        if not all_events:
            print("[-] No valid JSON data found inside the files.")
            return pd.DataFrame()

        df = pd.DataFrame(all_events)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df

    def filter_noise(self, df):
        high_value_ids = [
            'cowrie.login.success', 
            'cowrie.login.failed', 
            'cowrie.command.input', 
            'cowrie.session.file_download'
        ]
        # Check if eventid column exists before filtering
        if 'eventid' in df.columns:
            return df[df['eventid'].isin(high_value_ids)]
        else:
            print("[!] Warning: 'eventid' column missing from logs!")
            return df
