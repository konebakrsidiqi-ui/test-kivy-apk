from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        # Crée un label simple centré à l'écran
        return Label(
            text="Bonjour Mali !",
            font_size="24sp",
            color=(1, 1, 1, 1)  # Texte en blanc
        )

if __name__ == "__main__":
    TestApp().run()
