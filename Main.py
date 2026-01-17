import shutil
import pathlib
from pathlib import Path
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel,QFileDialog
from PySide6.QtCore import Slot
from PySide6 import QtCore, QtWidgets, QtGui
# Greetings

class myApp(QtWidgets.QWidget):


    
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Choose directory")
        self.button2 = QtWidgets.QPushButton("Copy")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button2)

        self.button.clicked.connect(self.Testo)
        self.button2.clicked.connect(self.test)


    @QtCore.Slot()
    def Testo(self):
        self.fileName = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "coś"
        )
        
        

    @QtCore.Slot()
    def test(self):
    
        home_dir = Path.home()
        
        test = pathlib.Path("/usr/share/plasma/desktoptheme/")
        dest = self.fileName
        test2 = pathlib.Path(f"{home_dir}/.local/share/plasma/look-and-feel/")

        shutil.copytree(test, dest, dirs_exist_ok=True)
        shutil.copytree(test2, dest, dirs_exist_ok=True)

        self.text.setText("zrobione ez?")






if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = myApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
    