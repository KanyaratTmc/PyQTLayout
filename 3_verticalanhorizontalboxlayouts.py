import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QHBoxLayout,QCheckBox,QRadioButton,QComboBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()

        btn1 = QComboBox()
        btn2 = QComboBox()

        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)

        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)

        self.setLayout(mainLayout)
        self.show()





def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()