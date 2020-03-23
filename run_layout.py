import sys
import hv_layout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # create an instance of Qapplication
    app = QApplication(sys.argv)
    # set up a main window
    main_window = QMainWindow()
    # create an instance of the class of layout
    ui = hv_layout.Ui_MainWindow()
    # put the layout into the main window
    ui.setupUi(main_window)
    # show the main window
    main_window.show()
    # exit
    sys.exit(app.exec_())
