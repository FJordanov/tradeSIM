# tradeSIM

A Python Flask web app for a trading simulator using the Alpha Vantage API. Features include:
- User authentication (login/signup)
- Profile management (profile picture, name, friends)
- Main trading page for browsing different stock types with real-time data

## Setup
1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```powershell
   pip install flask flask_sqlalchemy flask_login requests pillow
   ```
3. Set your Alpha Vantage API key as an environment variable:
   ```powershell
   $env:ALPHAVANTAGE_API_KEY = "your_api_key_here"
   ```
4. Run the app:
   ```powershell
   python app.py
   ```

## Notes
- Profile pictures are stored locally for demo purposes.
- Replace placeholder assets as needed.
- This is a demo/simulator and does not execute real trades.
