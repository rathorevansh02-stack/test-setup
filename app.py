import psycopg2

# Database Connection Details
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "0210" 
DB_PORT = "5432"

try:
    # 1. ESTABLISH CONNECTION: Open a tunnel to PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    
    # Create a cursor object (this executes your SQL statements)
    cursor = conn.cursor()
    print("🚀 Connection to PostgreSQL established successfully!\n")

    # ========================================================
    # PERFORMING CRUD OPERATIONS THROUGH PYTHON
    # ========================================================

    # 2. DROP & CREATE TABLE (Clean setup)
    print("🧹 Cleaning up and creating fresh table...")
    cursor.execute("DROP TABLE IF EXISTS player;")
    
    create_table_query = """
    CREATE TABLE player (
        id SERIAL PRIMARY KEY,
        level INT NOT NULL,
        name VARCHAR(100),
        power INT NOT NULL,
        rank VARCHAR(50) DEFAULT 'chuttad',
        hour_played INT NOT NULL
    );
    """
    cursor.execute(create_table_query)
    print("✅ Table 'player' created successfully.")

    # 3. INSERT (Create): Adding rows through Python variables
    print("📥 Inserting player records...")
    insert_query = """
    INSERT INTO player (level, name, power, hour_played, rank)
    VALUES (%s, %s, %s, %s, %s);
    """
    # Tuples containing your exact data values
    players_data = [
        (15, 'vishu', 4200, 12, 'chuttad'),
        (88, 'rathore', 95000, 450, 'monarch'),
        (42, 'kallu kaliya', 22000, 110, 'diamond II'),
        (5, 'ram rahim', 450, 2, 'chuttad'),
        (61, 'modiji dilfire ashique', 54000, 280, 'platinum I'),
        (12, 'rahul gandhi', 2100, 8, 'chuttad'),
        (75, 'lally yadav', 71000, 390, 'Immortal'),
        (23, 'kejri bal', 9800, 45, 'Silver III'),
        (3, 'choota hathi', 150, 1, 'chuttad'),
        (50, 'kankhajura', 38000, 195, 'Gold III')
    ]
    
    # Execute batch insertion
    cursor.executemany(insert_query, players_data)
    
    # CRITICAL: Always commit changes when altering data (INSERT, UPDATE, DELETE)
    conn.commit()
    print(f"✅ Successfully inserted {len(players_data)} rows.")

    # 4. SELECT (Read): Fetching data from database into Python variables
    print("\n📋 Fetching and displaying data from Python:")
    cursor.execute("SELECT id, name, level, power, rank FROM player ORDER BY id ASC;")
    records = cursor.fetchall()  # Pulls the records into a Python list
    
    print("-" * 75)
    for row in records:
        print(f"ID: {row[0]} | Name: {row[1]:<23} | Level: {row[2]:<3} | Power: {row[3]:<6} | Rank: {row[4]}")
    print("-" * 75)

    # 5. UPDATE: Changing values dynamically via code
    print("\n🔄 Updating 'rathore' to higher power...")
    cursor.execute("UPDATE player SET power = 99999 WHERE name = 'rathore';")
    conn.commit()

    # 6. DELETE: Removing a row via Python command
    print("❌ Deleting 'choota hathi' from database...")
    cursor.execute("DELETE FROM player WHERE name = 'choota hathi';")
    conn.commit()

    # Final read check to verify mutations
    print("\n📊 Verification Check after Update and Delete:")
    cursor.execute("SELECT name, power FROM player WHERE name IN ('rathore', 'choota hathi');")
    check_records = cursor.fetchall()
    print(f"Remaining matching records in DB: {check_records}")

    # ========================================================
    # CLOSING CHANNELS
    # ========================================================
    cursor.close()
    conn.close()
    print("\n🔒 Connection safely closed.")

except Exception as e:
    print(f"❌ An error occurred: {e}")