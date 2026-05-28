import psycopg2

def get_db_connection():
    """Opens and returns a live tunnel to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="0210",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"❌ Structural Connection Error: {e}")
        return None