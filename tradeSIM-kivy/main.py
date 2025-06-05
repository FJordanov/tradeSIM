import json
import hashlib
import smtplib
from email.message import EmailMessage
import os
import base64
from cryptography.fernet import Fernet
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from ui import LoginScreen, SignupScreen, ProfileScreen, TradingScreen

# --- Security Setup ---
ENCRYPTION_KEY = base64.urlsafe_b64encode(hashlib.sha256(b'tradeSIM_secret_key').digest())
cipher_suite = Fernet(ENCRYPTION_KEY)

# --- App Entry Point ---
class TradeSimApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(TradingScreen(name='trading'))
        return sm

if __name__ == '__main__':
    TradeSimApp().run()
