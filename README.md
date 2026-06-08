
# FinPulse ⚡ - Personal Finance Dashboard

FinPulse is a desktop application designed to track personal wealth and analyze expense distribution. Built with a focus on modern UI design and clean data architecture, it visualizes financial data stored securely in a relational database.

## 🚀 Tech Stack
* **Frontend GUI:** Python, CustomTkinter (Dark-mode optimized)
* **Data Visualization:** Matplotlib
* **Backend Database:** MySQL
* **Security:** `python-dotenv` for environment variable management

## 🧠 Architectural Decisions
* **Separation of Concerns:** Database logic (`database.py`) is decoupled from the presentation layer (`main.py`) to ensure the code is modular and easy to maintain.
* **Security:** Implemented parameterized SQL queries to prevent SQL injection and utilized environment variables to secure database credentials.
* **Robust Error Handling:** Integrated context managers to ensure database connections are safely terminated even during unexpected application closures.

## 🛠️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Biswajeet-99/ FinPulse-WealthTrack.git](https://github.com/Biswajeet-99/FinPulse-WealthTrack.git)
   cd FinPulse-WealthTrack
