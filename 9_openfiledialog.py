import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QFileDialog, QFontDialog, QColorDialog
from PyQt6.QtGui import QColor

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialogs")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        fileButton = QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)
        fontButton = QPushButton("Change Font")
        fontButton.clicked.connect(self.changeFont)
        colorButton = QPushButton("Change Color")
        colorButton.clicked.connect(self.changeColor)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addWidget(fontButton)
        hbox.addWidget(colorButton)
        hbox.addStretch()
        self.setLayout(vbox)
        self.show()

    def openFile(self):
        url = QFileDialog.getOpenFileName(self,"Open a file","","All File(*);;*txt")
        print(url)
        fileUrl = url[0]
        if fileUrl:
            file = open(fileUrl, 'r')
            content = file.read()
            self.editor.setText(content)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok :
            self.editor.setCurrentFont(font)

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.editor.setTextColor(color)

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()