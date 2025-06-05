# tradeSIM

A Python Kivy app for a trading simulator using the Alpha Vantage API. Features include:
- User authentication (login/signup)
- Profile management (profile picture, name, friends)
- Main trading page for browsing different stock types with real-time data

## Setup
1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```powershell
   pip install kivy cryptography requests
   ```
3. Set your Alpha Vantage API key as an environment variable (replace with your own key):
   ```powershell
   $env:ALPHAVANTAGE_API_KEY = "your-api_key"
   ```
4. Run the app:
   ```powershell
   python tradeSIM-kivy/main.py
   ```

## Notes
- Profile pictures and user data are stored locally for demo purposes.
- Replace placeholder assets as needed.
- This is a demo/simulator and does not execute real trades.
- The Flask version is deprecated; use the Kivy app for all new development.
