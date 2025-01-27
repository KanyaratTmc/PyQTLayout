import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout()
        for i in range(0, 3):
            for j in range(0, 3):
                btn = QPushButton(f"Button{i}{j}")
                self.gridLayout.addWidget(btn, i, j)
                btn.clicked.connect(self.clickMe)
        self.setLayout(self.gridLayout)
        self.show()

    def clickMe(self):
        buttonID = self.sender().text()
        if buttonID == "Button00":
            print("Button1 was clicked")
        elif buttonID == "Button01":
            print("Button2 was clicked")
        elif buttonID == "Button02":
            print("Button3 was clicked")

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()