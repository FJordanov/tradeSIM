from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Set a fixed window size and background color
Window.size = (600, 800)
Window.clearcolor = (0.97, 0.97, 1, 1)  # Light blue/white background

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.remember = False
        self.message = Label(text='', color=(0.9,0.2,0.2,1), font_size=16)
        outer = BoxLayout(orientation='vertical', padding=40, spacing=20, size_hint=(None, None), size=(400, 500), pos_hint={'center_x':0.5, 'center_y':0.5})
        with outer.canvas.before:
            Color(1, 1, 1, 1)  # Pure white background for better contrast
            self.bg_rect = RoundedRectangle(radius=[20], pos=outer.pos, size=outer.size)
        def update_bg_rect(*_):
            self.bg_rect.pos = outer.pos
            self.bg_rect.size = outer.size
        outer.bind(pos=update_bg_rect, size=update_bg_rect)
        outer.add_widget(Label(text='Login', font_size=28, color=(0.1,0.2,0.4,1), size_hint_y=None, height=40))
        outer.add_widget(self.message)
        self.username = TextInput(hint_text='Username', multiline=False, size_hint_y=None, height=40, background_color=(0.98,0.98,0.98,1), foreground_color=(0,0,0,1))
        self.password = TextInput(hint_text='Password', password=True, multiline=False, size_hint_y=None, height=40, background_color=(0.98,0.98,0.98,1), foreground_color=(0,0,0,1))
        outer.add_widget(self.username)
        outer.add_widget(self.password)
        self.remember_me = Button(text='Remember Me: OFF', size_hint_y=None, height=40, background_color=(0.85,0.9,1,1), color=(0.1,0.2,0.4,1))
        self.remember_me.bind(on_press=self.toggle_remember)
        outer.add_widget(self.remember_me)
        login_btn = Button(text='Login', size_hint_y=None, height=45, background_color=(0.1,0.5,0.2,1), color=(1,1,1,1))
        login_btn.bind(on_press=self.login)
        outer.add_widget(login_btn)
        signup_btn = Button(text='Go to Signup', size_hint_y=None, height=40, background_color=(0.2,0.4,0.8,1), color=(1,1,1,1))
        signup_btn.bind(on_press=self.go_to_signup)
        outer.add_widget(signup_btn)
        self.add_widget(Widget())  # Spacer
        self.add_widget(outer)
        self.add_widget(Widget())  # Spacer
        self.load_remembered()

    def toggle_remember(self, instance):
        self.remember = not self.remember
        self.remember_me.text = f'Remember Me: {"ON" if self.remember else "OFF"}'

    def login(self, instance):
        import json, hashlib, os, base64
        from cryptography.fernet import Fernet
        ENCRYPTION_KEY = base64.urlsafe_b64encode(hashlib.sha256(b'tradeSIM_secret_key').digest())
        cipher_suite = Fernet(ENCRYPTION_KEY)
        username = self.username.text.strip()
        password = self.password.text.strip()
        if not username or not password:
            self.message.text = 'Please enter both fields.'
            return
        user = self.load_user(username)
        if user and user['password'] == self.hash_password(password):
            self.message.text = ''
            if self.remember:
                self.save_remembered(username, password)
            else:
                self.clear_remembered()
            self.manager.current = 'profile'
        else:
            self.message.text = 'Invalid username or password.'

    def save_remembered(self, username, password):
        import json, base64, hashlib
        from cryptography.fernet import Fernet
        ENCRYPTION_KEY = base64.urlsafe_b64encode(hashlib.sha256(b'tradeSIM_secret_key').digest())
        cipher_suite = Fernet(ENCRYPTION_KEY)
        encrypted = cipher_suite.encrypt(password.encode()).decode()
        with open('remember.json', 'w') as f:
            json.dump({'username': username, 'password': encrypted}, f)

    def load_remembered(self):
        import json, os, base64, hashlib
        from cryptography.fernet import Fernet
        ENCRYPTION_KEY = base64.urlsafe_b64encode(hashlib.sha256(b'tradeSIM_secret_key').digest())
        cipher_suite = Fernet(ENCRYPTION_KEY)
        if os.path.exists('remember.json'):
            try:
                with open('remember.json', 'r') as f:
                    data = json.load(f)
                self.username.text = data.get('username', '')
                encrypted = data.get('password', '')
                if encrypted:
                    self.password.text = cipher_suite.decrypt(encrypted.encode()).decode()
                self.remember = True
                self.remember_me.text = 'Remember Me: ON'
            except Exception:
                pass

    def clear_remembered(self):
        import os
        if os.path.exists('remember.json'):
            os.remove('remember.json')

    def hash_password(self, password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def load_user(self, username):
        import json, os
        if not os.path.exists('users.json'):
            return None
        with open('users.json', 'r') as f:
            users = json.load(f)
        return users.get(username)

    def go_to_signup(self, instance):
        self.manager.current = 'signup'

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message = Label(text='', color=(0.9,0.2,0.2,1), font_size=16)
        outer = BoxLayout(orientation='vertical', padding=40, spacing=20, size_hint=(None, None), size=(400, 550), pos_hint={'center_x':0.5, 'center_y':0.5})
        with outer.canvas.before:
            Color(1, 1, 1, 1)  # Pure white background for better contrast
            self.bg_rect = RoundedRectangle(radius=[20], pos=outer.pos, size=outer.size)
        def update_bg_rect(*_):
            self.bg_rect.pos = outer.pos
            self.bg_rect.size = outer.size
        outer.bind(pos=update_bg_rect, size=update_bg_rect)
        outer.add_widget(Label(text='Sign Up', font_size=28, color=(0.1,0.2,0.4,1), size_hint_y=None, height=40))
        outer.add_widget(self.message)
        self.username = TextInput(hint_text='Username', multiline=False, size_hint_y=None, height=40, background_color=(0.98,0.98,0.98,1), foreground_color=(0,0,0,1))
        self.email = TextInput(hint_text='Email', multiline=False, size_hint_y=None, height=40, background_color=(0.98,0.98,0.98,1), foreground_color=(0,0,0,1))
        self.password = TextInput(hint_text='Password', password=True, multiline=False, size_hint_y=None, height=40, background_color=(0.98,0.98,0.98,1), foreground_color=(0,0,0,1))
        outer.add_widget(self.username)
        outer.add_widget(self.email)
        outer.add_widget(self.password)
        signup_btn = Button(text='Sign Up', size_hint_y=None, height=45, background_color=(0.1,0.5,0.2,1), color=(1,1,1,1))
        signup_btn.bind(on_press=self.signup)
        outer.add_widget(signup_btn)
        login_btn = Button(text='Go to Login', size_hint_y=None, height=40, background_color=(0.2,0.4,0.8,1), color=(1,1,1,1))
        login_btn.bind(on_press=self.go_to_login)
        outer.add_widget(login_btn)
        self.add_widget(Widget())
        self.add_widget(outer)
        self.add_widget(Widget())

    def signup(self, instance):
        import json, hashlib, os, base64
        from cryptography.fernet import Fernet
        from email.message import EmailMessage
        import smtplib
        ENCRYPTION_KEY = base64.urlsafe_b64encode(hashlib.sha256(b'tradeSIM_secret_key').digest())
        cipher_suite = Fernet(ENCRYPTION_KEY)
        username = self.username.text.strip()
        email = self.email.text.strip()
        password = self.password.text.strip()
        if not username or not email or not password:
            self.message.text = 'All fields are required.'
            return
        if '@' not in email or '.' not in email:
            self.message.text = 'Invalid email address.'
            return
        users = self.load_users()
        if username in users:
            self.message.text = 'Username already exists.'
            return
        hashed = self.hash_password(password)
        encrypted = cipher_suite.encrypt(password.encode()).decode()
        users[username] = {'email': email, 'password': hashed, 'encrypted': encrypted}
        self.save_users(users)
        self.send_email(email, username)
        self.message.text = 'Registration successful! Check your email.'
        self.username.text = ''
        self.email.text = ''
        self.password.text = ''

    def go_to_login(self, instance):
        self.manager.current = 'login'

    def hash_password(self, password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def load_users(self):
        import json, os
        if not os.path.exists('users.json'):
            return {}
        with open('users.json', 'r') as f:
            return json.load(f)

    def save_users(self, users):
        import json
        with open('users.json', 'w') as f:
            json.dump(users, f)

    def send_email(self, to_email, username):
        from email.message import EmailMessage
        import smtplib
        FROM = 'fif.jordanov@gmail.com'
        PASS = 'your_email_password'
        SMTP = 'smtp.gmail.com'
        PORT = 587
        msg = EmailMessage()
        msg['Subject'] = 'Welcome to tradeSIM!'
        msg['From'] = FROM
        msg['To'] = to_email
        msg.set_content(f'Hello {username},\n\nThank you for registering at tradeSIM!')
        try:
            with smtplib.SMTP(SMTP, PORT) as server:
                server.starttls()
                server.login(FROM, PASS)
                server.send_message(msg)
        except Exception as e:
            print('Email error:', e)

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Profile', font_size=26, color=(0.1,0.2,0.4,1)))
        layout.add_widget(Label(text='Welcome! (Profile features go here)', color=(0.2,0.2,0.2,1)))
        trading_btn = Button(text='Go to Trading', background_color=(0.1,0.5,0.2,1), color=(1,1,1,1))
        trading_btn.bind(on_press=self.go_to_trading)
        layout.add_widget(trading_btn)
        self.add_widget(layout)

    def go_to_trading(self, instance):
        self.manager.current = 'trading'

class TradingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Menu bar (vertical)
        menu_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=180, spacing=8)
        menu_layout.add_widget(Button(text='Home', on_press=self.go_to_profile, background_color=(0.2,0.4,0.8,1), color=(1,1,1,1)))
        menu_layout.add_widget(Button(text='Portfolio', background_color=(0.3,0.6,0.9,1), color=(1,1,1,1)))
        menu_layout.add_widget(Button(text='History', background_color=(0.4,0.7,1,1), color=(1,1,1,1)))
        menu_layout.add_widget(Button(text='Settings', background_color=(0.5,0.8,1,1), color=(1,1,1,1)))
        main_layout.add_widget(menu_layout)
        # Search bar
        search_layout = BoxLayout(size_hint_y=None, height=50, spacing=5, padding=[0,10,0,10])
        self.search_input = TextInput(hint_text='Search stocks...', multiline=False, size_hint_x=0.7, size_hint_y=None, height=40, background_color=(0.98,0.98,0.98,1), foreground_color=(0,0,0,1))
        search_btn = Button(text='Search', on_press=self.search_stock, size_hint_x=0.3, size_hint_y=None, height=40, background_color=(0.1,0.5,0.2,1), color=(1,1,1,1))
        search_layout.add_widget(self.search_input)
        search_layout.add_widget(search_btn)
        main_layout.add_widget(search_layout)
        # Trading table (scrollable)
        scroll = ScrollView(size_hint=(1, 1))
        self.table = BoxLayout(orientation='vertical', spacing=2, size_hint_y=None)
        self.table.bind(minimum_height=self.table.setter('height'))
        self.populate_table()
        scroll.add_widget(self.table)
        main_layout.add_widget(scroll)
        self.add_widget(main_layout)

    def go_to_profile(self, instance):
        self.manager.current = 'profile'

    def search_stock(self, instance):
        query = self.search_input.text.strip()
        self.table.clear_widgets()
        self.table.add_widget(Label(text=f'Search results for: {query} (Demo)', font_size=18))
        # ...populate with search results...

    def populate_table(self):
        self.table.clear_widgets()
        self.table.add_widget(Label(text='Symbol | Name | Price | Change | Volume | Chart | RSI | MACD | News', font_size=16))
        for symbol in ['AAPL', 'GOOGL', 'MSFT', 'TSLA']:
            self.table.add_widget(Label(text=f'{symbol} | Example | $100 | +1.2% | 1M | [Chart] | 55 | 1.2 | [News]'))
        # TODO: Add interactive selection and analysis tools
