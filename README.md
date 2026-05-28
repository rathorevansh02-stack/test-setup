# Python & PostgreSQL Modular Database Pipeline

A backend project structure demonstrating how to connect a Python application to a local PostgreSQL server using an industry-standard, modular architecture.

## 📁 Project Architecture
- `config/`: Contains secure database connection logic.
- `queries/`: Reserved for storing SQL lookup scripts.
- `utils/`: Reserved for backend helper functions.
- `.env`: Holds secure system credentials (hidden from version control).
- `main.py`: The central execution file that boots up the application.

## 🛠️ Tech Stack
- **Language:** Python
- **Database Engine:** PostgreSQL
- **Database Driver:** `psycopg2-binary`
- **IDE:** Visual Studio Code