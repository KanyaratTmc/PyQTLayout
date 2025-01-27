import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        helpMenu = menubar.addMenu("Help")
        #######Sub Menu##########################
        new = QAction("New Project",self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)
        openMenu = QAction("Open",self)
        file.addAction(openMenu)
        exitMenu = QAction("Exit",self)    
        exitMenu.setIcon(QIcon("icons/exit.png"))
        exitMenu.triggered.connect(self.exitFunc)     
        file.addAction(exitMenu)   
        ############Tool Bar################
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon('icons/folder.png'),"New",self)
        tb.addAction(newTb)
        openTb = QAction(QIcon('icons/empty.png'),"Open",self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon('icons/save.png'),"Save",self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon('icons/exit.png'),"Exit",self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)
        tb.actionTriggered.connect(self.btnFunc)
        self.show()

    def exitFunc(self):
        mbox = QMessageBox.information(self,"Warning","Are you sure to exit ?",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)
        if mbox == QMessageBox.StandardButton.Yes :
            sys.exit()

    def btnFunc(self,btn):
        if btn.text() == "New":
            print("You clicked new button")
        elif btn.text() == "Open":
            print("You clicked open button")
        else :
            print("You clicked save button")



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()