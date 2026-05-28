def setup_player_table(conn):
    """Creates a fresh player table."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS player;")
    
    cursor.execute("""
    CREATE TABLE player (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        level INT NOT NULL,
        power INT NOT NULL
    );
    """)
    
    # Insert some starter data
    cursor.execute("""
    INSERT INTO player (name, level, power) VALUES 
    ('vishu', 15, 4200),
    ('rathore', 88, 95000),
    ('kallu kaliya', 42, 22000);
    """)
    
    conn.commit()
    cursor.close()
    print("🧹 [QUERIES] Fresh player table initialized with starter data.")

def fetch_all_players(conn):
    """Fetches and returns all player rows from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, level, power FROM player ORDER BY id ASC;")
    records = cursor.fetchall()
    cursor.close()
    return records

def add_custom_player(conn, name, level, power):
    """Inserts a user-defined player securely into the table using dynamic parameters."""
    cursor = conn.cursor()
    # Using %s placeholders prevents malicious SQL injections!
    cursor.execute(
        "INSERT INTO player (name, level, power) VALUES (%s, %s, %s);",
        (name, level, power)
    )
    conn.commit()
    cursor.close()
    print(f"✅ [DATABASE] {name} successfully logged to central registry!")