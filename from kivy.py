from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse
from kivy.uix.popup import Popup

class Dot(Widget):
    def __init__(self, col, idx, callback, **kwargs):
        super().__init__(**kwargs)
        self.col = col
        self.idx = idx
        self.callback = callback
        self.selected = False
        self.disabled = False
        self.size_hint = (None, None)
        self.size = (80, 80)

        with self.canvas:
            self.color = Color(1, 1, 1, 1)  # white dot initially
            self.circle = Ellipse(pos=self.pos, size=self.size)

        self.bind(pos=self.update_circle, size=self.update_circle)

    def update_circle(self, *args):
        self.circle.pos = self.pos
        self.circle.size = self.size

    def on_touch_down(self, touch):
        if self.disabled:
            return False
        if self.collide_point(*touch.pos):
            self.callback(self.col, self.idx)
            return True
        return False

    def select(self):
        self.selected = True
        self.color.rgb = (1, 0, 0)  # red

    def unselect(self):
        self.selected = False
        self.color.rgb = (1, 1, 1)  # white

    def disable(self):
        self.disabled = True
        self.color.rgb = (0.5, 0.5, 0.5)  # gray

    def reset(self):
        self.disabled = False
        self.unselect()

class DotGame(App):
    def build(self):
        self.columns = [5, 4, 3]
        self.current_player = 1

        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.status_label = Label(text=f"Player {self.current_player}'s Turn", font_size=30, size_hint_y=None, height=50)
        root.add_widget(self.status_label)

        self.columns_layout = BoxLayout(spacing=40, padding=20)
        root.add_widget(self.columns_layout)

        buttons_layout = BoxLayout(size_hint_y=None, height=120, spacing=20, padding=[0,10,0,10])

        self.end_turn_btn = Button(text="End Turn", font_size=24)
        self.end_turn_btn.bind(on_press=self.on_end_turn)
        buttons_layout.add_widget(self.end_turn_btn)

        self.restart_btn = Button(text="Restart", font_size=24)
        self.restart_btn.bind(on_press=self.on_restart)
        buttons_layout.add_widget(self.restart_btn)

        root.add_widget(buttons_layout)

        self.reset_game()

        return root

    def reset_game(self):
        # Clear existing dots layout
        self.columns_layout.clear_widgets()
        self.dots = [[], [], []]
        self.selected_column = None
        self.selected_dots = set()
        self.current_player = 1
        self.status_label.text = f"Player {self.current_player}'s Turn"

        for col_index, dot_count in enumerate(self.columns):
            col_layout = BoxLayout(orientation='vertical', spacing=30)
            for dot_index in range(dot_count):
                dot = Dot(col_index, dot_index, self.on_dot_press)
                self.dots[col_index].append(dot)
                col_layout.add_widget(dot)
            self.columns_layout.add_widget(col_layout)

    def on_dot_press(self, col, idx):
        dot = self.dots[col][idx]
        if dot.disabled:
            return

        if self.selected_column is None:
            self.selected_column = col
        elif self.selected_column != col:
            self.show_popup("Invalid Selection", "You can only select dots from one column per turn.")
            return

        if dot.selected:
            dot.unselect()
            self.selected_dots.remove(idx)
        else:
            dot.select()
            self.selected_dots.add(idx)

    def on_end_turn(self, instance):
        if self.selected_column is None or not self.selected_dots:
            self.show_popup("No Selection", "You must select at least one dot before ending your turn.")
            return

        for idx in self.selected_dots:
            dot = self.dots[self.selected_column][idx]
            dot.disable()

        self.selected_column = None
        self.selected_dots.clear()

        if all(dot.disabled for col in self.dots for dot in col):
            self.show_popup("Game Over", f"Player {self.current_player} wins!")
            self.status_label.text = "Game Over"
        else:
            self.current_player = 2 if self.current_player == 1 else 1
            self.status_label.text = f"Player {self.current_player}'s Turn"

    def on_restart(self, instance):
        self.reset_game()

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, font_size=20),
                      size_hint=(None, None), size=(350, 220))
        popup.open()

if __name__ == '__main__':
    DotGame().run()
