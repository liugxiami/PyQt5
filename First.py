import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore

if __name__ == '__main__':
    # create an instance of QApplication
    app = QApplication(sys.argv)
    # create a window
    w = QWidget()
    # set the size of the window
    w.resize(400, 200)
    # move the window
    w.move(300, 300)
    # set the title for the window
    w.setWindowTitle('My first pyqt5 app!')
    # show the window
    w.show()

    # into the mainloop and exit the app
    sys.exit(app.exec_())

