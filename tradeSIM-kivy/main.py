from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Login', font_size=24))
        self.username = TextInput(hint_text='Username', multiline=False)
        self.password = TextInput(hint_text='Password', password=True, multiline=False)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        login_btn = Button(text='Login')
        login_btn.bind(on_press=self.login)
        layout.add_widget(login_btn)
        signup_btn = Button(text='Go to Signup')
        signup_btn.bind(on_press=self.go_to_signup)
        layout.add_widget(signup_btn)
        self.add_widget(layout)

    def login(self, instance):
        # Add authentication logic here
        self.manager.current = 'profile'

    def go_to_signup(self, instance):
        self.manager.current = 'signup'

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Sign Up', font_size=24))
        self.username = TextInput(hint_text='Username', multiline=False)
        self.email = TextInput(hint_text='Email', multiline=False)
        self.password = TextInput(hint_text='Password', password=True, multiline=False)
        layout.add_widget(self.username)
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        signup_btn = Button(text='Sign Up')
        signup_btn.bind(on_press=self.signup)
        layout.add_widget(signup_btn)
        login_btn = Button(text='Go to Login')
        login_btn.bind(on_press=self.go_to_login)
        layout.add_widget(login_btn)
        self.add_widget(layout)

    def signup(self, instance):
        # Add signup logic here
        self.manager.current = 'login'

    def go_to_login(self, instance):
        self.manager.current = 'login'

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Profile', font_size=24))
        layout.add_widget(Label(text='Welcome! (Profile features go here)'))
        trading_btn = Button(text='Go to Trading')
        trading_btn.bind(on_press=self.go_to_trading)
        layout.add_widget(trading_btn)
        self.add_widget(layout)

    def go_to_trading(self, instance):
        self.manager.current = 'trading'

class TradingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Trading', font_size=24))
        layout.add_widget(Label(text='Browse stocks here.'))
        profile_btn = Button(text='Back to Profile')
        profile_btn.bind(on_press=self.go_to_profile)
        layout.add_widget(profile_btn)
        self.add_widget(layout)

    def go_to_profile(self, instance):
        self.manager.current = 'profile'

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
