import sqlite3


conn = sqlite3.connect('threats.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ioc TEXT NOT NULL,
        ioc_type TEXT NOT NULL,
        malicious INTEGER,
        suspicious INTEGER,
        harmless INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()

print("[+] Database 'threats.db' created successfully!")
