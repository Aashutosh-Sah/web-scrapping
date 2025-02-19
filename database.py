import sqlite3

# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect("wikipedia_searches.db")
    return conn

# Create table if not exists
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wiki_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT UNIQUE,
            summary TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Insert data into database
def insert_data(topic, summary):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO wiki_data (topic, summary) VALUES (?, ?)", (topic, summary))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Data already exists in the database.")
    conn.close()

# Fetch data from database
def fetch_data(topic):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT summary FROM wiki_data WHERE topic = ?", (topic,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Initialize table on import
create_table()
