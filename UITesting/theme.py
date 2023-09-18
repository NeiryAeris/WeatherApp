# im testing pyside6
import random
import sys
from PySide6 import QtCore, QtWidgets, QtGui


# Here gose nothing
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Neiry", "Hey Fox", "Hola Wolf", "Hi Lamb"]

        self.button = QtWidgets.QPushButton("click here pls")
        self.text = QtWidgets.QLabel("Hello", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
