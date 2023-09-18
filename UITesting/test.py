import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.city_label = QLabel("Enter City:")
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather")

        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.get_weather_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.get_weather_button.clicked.connect(self.get_weather)

        self.central_widget.setLayout(self.layout)

    def get_weather(self):
        city = self.city_input.text()
        if not city:
            QMessageBox.warning(self, "Warning", "Please enter a city.")
            return

        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = 'YOUR_API_KEY'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            data = response.json()

            if data.get('main'):
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                self.result_label.setText(f"Temperature: {temperature}°C\nDescription: {description}")
            else:
                QMessageBox.warning(self, "Error", "City not found.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
