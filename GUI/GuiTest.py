from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('test')
    
        self.initui()
        
        
    def initui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('asd')
        self.label.move(50,50)
    
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click me')
        self.b1.clicked.connect(self.clicked)    
        
    def clicked(self):
        self.label.setText('you pressed the button')
        self.update()
    def update(self):
        self.label.adjustSize()
    






def window():
    app = QApplication(sys.argv)
    win = mywindow()
    
  
    win.show()
    sys.exit(app.exec_())
    
window()


