import sqlite3

def init_db():
    conn = sqlite3.connect("repos.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS searches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT,
        repo TEXT,
        stars INTEGER,
        forks INTEGER,
        language TEXT,
        UNIQUE(owner, repo)
    )
     """)
    
    conn.commit()
    conn.close()
    
def save_search(owner, repo=None, stars=None, forks=None, language=None):
        conn = sqlite3.connect("repos.db")
        cursor = conn.cursor()

        if repo is None:
            cursor.execute("SELECT id FROM searches WHERE owner = ?", (owner,))
        else:
            cursor.execute("SELECT id FROM searches WHERE owner = ? AND repo = ?", (owner, repo))

        existing_search = cursor.fetchone()

        if not existing_search:
            cursor.execute("""
            INSERT INTO searches (owner, repo, stars, forks, language)
            VALUES (?,?,?,?,?)
            """, (owner, repo, stars, forks, language))
    
        conn.commit()
        conn.close()