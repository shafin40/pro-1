from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

class ThermalExpansionCalculator(MDApp):
    def build(self):
        self.title = "Thermal Expansion Calculator"
        self.result_label = MDLabel()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        choice_label = MDLabel(text="Choose the type of thermal expansion you want to calculate:")
        layout.add_widget(choice_label)

        self.choice_var = '1'
        self.choice_buttons = []
        for choice_text, choice_value in [("Calculate Alpha (Linear Expansion)", '1'),
                                          ("Calculate Beta (Cubical Expansion)", '2'),
                                          ("Calculate Gamma (Volumetric Expansion)", '3')]:
            choice_button = MDRaisedButton(text=choice_text)
            choice_button.bind(on_release=self.set_choice)
            layout.add_widget(choice_button)
            self.choice_buttons.append((choice_button, choice_value))

        input_labels = ["Enter the initial value:", "Enter the final value:", "Enter the temperature change (in Celsius or Kelvin):"]
        self.input_entries = []
        for label_text in input_labels:
            layout.add_widget(MDLabel(text=label_text))
            input_entry = MDTextField()
            layout.add_widget(input_entry)
            self.input_entries.append(input_entry)

        calculate_button = MDRaisedButton(text="Calculate")
        calculate_button.bind(on_release=self.calculate)
        layout.add_widget(calculate_button)

        layout.add_widget(self.result_label)

        return layout

    def set_choice(self, instance):
        for button, value in self.choice_buttons:
            if instance == button:
                self.choice_var = value

    def calculate_alpha(self, L1, L2, temperature_change):
        return (L2 - L1) / (L1 * temperature_change)

    def calculate_beta(self, L1, L2, temperature_change):
        alpha = self.calculate_alpha(L1, L2, temperature_change)
        beta = 3 * alpha
        return beta

    def calculate_gamma(self, V1, V2, temperature_change):
        return (V2 - V1) / (V1 * temperature_change)

    def calculate(self, instance):
        try:
            if self.choice_var == '1':
                L1 = float(self.input_entries[0].text)
                L2 = float(self.input_entries[1].text)
                temperature_change = float(self.input_entries[2].text)
                alpha = self.calculate_alpha(L1, L2, temperature_change)
                self.result_label.text = f"The coefficient of linear expansion (alpha) is {alpha:.6f} 1/°C or 1/K."
            elif self.choice_var == '2':
                L1 = float(self.input_entries[0].text)
                L2 = float(self.input_entries[1].text)
                temperature_change = float(self.input_entries[2].text)
                beta = self.calculate_beta(L1, L2, temperature_change)
                self.result_label.text = f"The coefficient of cubical expansion (beta) is {beta:.6f} 1/°C or 1/K."
            elif self.choice_var == '3':
                V1 = float(self.input_entries[0].text)
                V2 = float(self.input_entries[1].text)
                temperature_change = float(self.input_entries[2].text)
                gamma = self.calculate_gamma(V1, V2, temperature_change)
                self.result_label.text = f"The coefficient of volumetric expansion (gamma) is {gamma:.6f} 1/°C or 1/K."
        except ValueError:
            self.show_error_popup("Invalid input. Please enter valid numeric values.")

    def show_error_popup(self, error_message):
        dialog = MDDialog(title='Error', text=error_message)
        dialog.open()

if __name__ == '__main__':
    ThermalExpansionCalculator().run()
