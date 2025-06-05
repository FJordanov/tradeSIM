# tradeSIM Kivy App

A native Python Android trading simulator using Kivy. Features:
- Login/Signup screens
- Profile management (to be implemented)
- Main trading page (to be implemented)

## How to Run
1. Install Kivy:
   ```powershell
   pip install kivy
   ```
2. Set your Alpha Vantage API key as an environment variable (replace with your own key):
   ```powershell
   $env:ALPHAVANTAGE_API_KEY = "your-api_key"
   ```
3. Run the app:
   ```powershell
   python main.py
   ```

## Android APK
To build for Android, use Buildozer (Linux/WSL required):
```bash
pip install buildozer
buildozer init
buildozer -v android debug
```

## Note
This folder is for the Kivy version only. The Flask files can be deleted if you are moving forward with Kivy.
