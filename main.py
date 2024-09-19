import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
# from kivy_garden.svg import Svg

class CocoPayApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add PNG image to layout (replace 'your_image.png' with the actual file path)
        #img = Image(source='your_image.png')  # Replace with your PNG file path
        #layout.add_widget(img)

        # Label to display the generated number
        self.random_number_label = Label(text="Random number will appear here")
        layout.add_widget(self.random_number_label)

        # Button layout to center the button
        button_layout = BoxLayout()

        # Button to generate random number
        button = Button(text="CocoPay", size_hint=(None, None), size=(200, 50),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.generate_random_number)

        # Center the button
        button_layout.add_widget(Widget())  # Add spacer widget to the left
        button_layout.add_widget(button)  # Add the actual button
        button_layout.add_widget(Widget())  # Add spacer widget to the right

        layout.add_widget(button_layout)

        return layout

    def generate_random_number(self, instance):
        # Generate a random number and display it on the label
        random_number = random.randint(1, 1000)
        self.random_number_label.text = f"Random Number: {random_number}"

# Run the app
if __name__ == '__main__':
    CocoPayApp().run()
