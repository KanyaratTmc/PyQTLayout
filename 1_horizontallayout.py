import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        hbox = QHBoxLayout()
        button1 = QPushButton("Button1",self)
        button2 = QPushButton("Button2",self)
        button3 = QPushButton("Button3",self)
        hbox.addStretch()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        hbox.addStretch()
        self.setLayout(hbox)
        self.show()




def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()