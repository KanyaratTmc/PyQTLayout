import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider Widget")
        self.setGeometry(350, 150, 600, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getValue)
        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.slider)
        self.setLayout(vbox)

        self.show()

    def getValue(self):
        val = self.slider.value()
        print(val)
        self.text1.setText(str(val))

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()