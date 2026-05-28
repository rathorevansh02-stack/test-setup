import logging
from config.db_connection import get_db_connection
from queries.player_queries import setup_player_table, fetch_all_players, add_custom_player
from utils.input_helpers import get_clean_integer

# Configure Log Stream
logging.basicConfig(filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def show_menu():
    print("\n=== 🎮 CENTRAL DATA TERMINAL ===")
    print("1. View Current Registry")
    print("2. Register New Operator Profile")
    print("3. Wipe & Reset Database Table")
    print("4. Shutdown System")
    return input("Select Action Protocol (1-4): ")

def start_terminal():
    logging.info("Interactive control center loop initialized.")
    conn = get_db_connection()
    if conn is None: return

    while True:
        choice = show_menu()

        if choice == "1":
            players = fetch_all_players(conn)
            print("\n📋 LIVE REGISTRY ROWS:")
            print("-" * 50)
            for p in players:
                print(f"ID: {p[0]} | Name: {p[1]:<15} | Level: {p[2]:<3} | Power: {p[3]}")
            print("-" * 50)
            logging.info("Registry rows fetched and viewed.")

        elif choice == "2":
            name = input("Enter Operator Name: ")
            level = get_clean_integer("Enter Starting Level: ")
            power = get_clean_integer("Enter Computed Power Rating: ")
            
            add_custom_player(conn, name, level, power)
            logging.info(f"Dynamically registered player profile: {name}")

        elif choice == "3":
            confirm = input("⚠️ Are you sure you want to reset table data? (y/n): ")
            if confirm.lower() == 'y':
                setup_player_table(conn)
                logging.warning("User executed database structure factory reset protocol.")

        elif choice == "4":
            print("\n🔒 Cutting data links... Shutting down core engine node safely.")
            conn.close()
            logging.info("System closed cleanly via control operator signal.")
            break
        else:
            print("❌ Unknown protocol. Select a valid action code.")

if __name__ == "__main__":
    start_terminal()