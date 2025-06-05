# tradeSIM

A Python Kivy app for a trading simulator using the Alpha Vantage API. Features include:
- User authentication (login/signup)
- Profile management (profile picture, name, friends)
- Main trading page for browsing different stock types with real-time data

## Step-by-Step Guide to Run on a New Device

1. **Install Python 3.8 or newer**
   - Download from https://www.python.org/downloads/ and follow the installer instructions.
   - Make sure to check "Add Python to PATH" during installation.

2. **Open a terminal (PowerShell on Windows)**
   - Navigate to the project folder:
     ```powershell
     cd path\to\tradeSIM
     ```

3. **(Optional but recommended) Create a virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. **Install required dependencies**
   ```powershell
   pip install kivy cryptography requests
   ```

5. **Get your Alpha Vantage API key**
   - Sign up at https://www.alphavantage.co/support/#api-key to get a free API key.

6. **Set your Alpha Vantage API key as an environment variable**
   ```powershell
   $env:ALPHAVANTAGE_API_KEY = "your-api_key"
   ```
   - Replace `your-api_key` with your actual key from Alpha Vantage.

7. **Run the Kivy app**
   ```powershell
   python tradeSIM-kivy/main.py
   ```

8. **Login or Sign Up**
   - On first run, use the Sign Up screen to create a new user.
   - After registration, log in to access the profile and trading screens.

## Notes
- Profile pictures and user data are stored locally for demo purposes.
- Replace placeholder assets as needed.
- This is a demo/simulator and does not execute real trades.
- The Flask version is deprecated; use the Kivy app for all new development.
