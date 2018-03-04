import sys
import time
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import gui.mainwindowUi
import gui.dialogUi
import mainView
import mainController

class MainWindow(QMainWindow, gui.mainwindowUi.Ui_MainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self) # gets defined in the UI file
        
        view = mainView.MainView(self)
        
        dialog = Dialog()
        
        controller.setup(dialog, view)
        
        self.actionQuit.triggered.connect(self.close) # Quit menu item or shortcut triggered
        self.pushButton_waveBrowse.clicked.connect(view.browseWaveFile)
        self.pushButton_transBrowse.clicked.connect(view.browseTransFile)
        self.pushButton_mappingBrowse.clicked.connect(view.browseMappingFile)
        self.radioButton_selectWaveform.clicked.connect(view.en_selectWave)
        self.radioButton_loadWaveFile.clicked.connect(view.en_loadWaveFile)
        self.pushButton_addRow.clicked.connect(view.addEmptyRow)
        self.lineEdit_transFileName.textChanged.connect(lambda: view.updateTransTable(self.lineEdit_transFileName.text()))
        self.lineEdit_mappingFileName.textChanged.connect(lambda: view.updateMappingTable(self.lineEdit_mappingFileName.text()))
        
        self.pushButton_begin.clicked.connect(controller.validateAcqInput)
        self.pushButton_runTest.clicked.connect(controller.validateTestInput)
        

class Dialog(QDialog, gui.dialogUi.Ui_Dialog):
    def __init__(self):
        super().__init__(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint) # remove ? tooltip 
        self.setupUi(self)
    
    def sendMsg(self, msg, color='black'):
        self.textBrowser_msgs.append("<p style='color:%s';>%s</p>" % (color,msg))
        
    def clear(self):
        self.textBrowser_msgs.clear()
        
        
def main():
    app = QApplication(sys.argv)
    controller = mainController.MainController()
    window = MainWindow(controller)
    window.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()