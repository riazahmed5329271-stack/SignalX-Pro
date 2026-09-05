from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random


class SignalApp(App):

    def build(self):

        self.time_left = 60

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        self.title = Label(
            text="ADVANCED SIGNAL BOT",
            font_size=24
        )

        self.signal = Label(
            text="WAITING...",
            font_size=40
        )

        self.timer = Label(
            text="Time: 60",
            font_size=25
        )

        self.button = Button(
            text="GET SIGNAL",
            size_hint=(1,0.3)
        )

        self.button.bind(
            on_press=self.get_signal
        )

        layout.add_widget(self.title)
        layout.add_widget(self.signal)
        layout.add_widget(self.timer)
        layout.add_widget(self.button)

        return layout


    def get_signal(self, instance):

        result = random.choice(["BUY","SELL"])

        if result == "BUY":
            self.signal.text = "🟢 BUY"
            self.signal.color = (0,1,0,1)

        else:
            self.signal.text = "🔴 SELL"
            self.signal.color = (1,0,0,1)

        self.time_left = 60

        Clock.schedule_interval(
            self.countdown,1
        )


    def countdown(self, dt):

        self.time_left -= 1

        self.timer.text = "Time: " + str(self.time_left)

        if self.time_left <= 0:
            self.timer.text = "New Signal Ready"
            return False



SignalApp().run()