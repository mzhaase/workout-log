from kivy.app import App
from kivy.uix.widget import Widget


class HomeScreen(Widget):
    pass


class WorkoutLogger(App):
    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    WorkoutLogger().run()