import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLabel, QLineEdit, QHBoxLayout, QComboBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        formLayout = QFormLayout()
        name_txt = QLabel("Name : ")
        name_input = QLineEdit()
        surname_txt = QLabel("Surname : ")
        surname_input = QLineEdit()
        combo = QComboBox()
        combo.addItems(["Thai","USA","China"])   
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        formLayout.addRow(name_txt,name_input)
        formLayout.addRow(surname_txt,surname_input)
        formLayout.addRow(QLabel("Country : "),combo)
        formLayout.addRow(hbox)

        self.setLayout(formLayout)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()