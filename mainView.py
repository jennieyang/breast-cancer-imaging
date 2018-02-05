import PyQt5
from PyQt5.QtWidgets import *

class MainView():
    def __init__(self, form, inputValidator):
        self.form = form
        self.iv = inputValidator
    
    def setParams(self):
        self.iv.setTransSeq(self.getTransConfig)
        self.iv.setWaveFile(self.form.lineEdit_waveFileName.text())
        self.iv.setWaveType(self.form.comboBox_waveform.currentText())
        self.iv.setAmp(self.form.lineEdit_amplitude.text())
        self.iv.setFreq(self.form.lineEdit_freq.text())
        self.iv.setNumSamps(self.form.lineEdit_numSamps.text())
        self.iv.setSampRate(self.form.lineEdit_sampRate.text())
        self.iv.validate()
    
    def getTransConfig(self):
        transConfig = []
        for r in range(0,self.form.tableWidget_transConfig.rowCount()):
            txList = self.form.tableWidget_transConfig.item(r,0).text()
            rxList = self.form.tableWidget_transConfig.item(r,1).text()
            transConfig.append([txList, rxList])
        return transConfig
    
    def getFile(self, lineEditWidget, nameFilters):
        dlg = QFileDialog()
        dlg.setNameFilters(nameFilters)
        if dlg.exec_():
            filePath = dlg.selectedFiles()[0]
            lineEditWidget.setText(filePath)

    def browseWaveFile(self):
        self.getFile(self.form.lineEdit_waveFileName, ['Text Files (*.txt)', 'All Files (*.*)'])
        
    def browseTransFile(self):
        self.getFile(self.form.lineEdit_transFileName, ['INI Files (*.ini)', 'All Files (*.*)'])
    
    def en_selectWave(self):
        self.form.widget_loadWaveFile.setEnabled(False)
        self.form.widget_selectWaveform.setEnabled(True)

    def en_loadWaveFile(self):
        self.form.widget_loadWaveFile.setEnabled(True)
        self.form.widget_selectWaveform.setEnabled(False)

    def createTable(self):
        self.form.tableWidget_transConfig.setColumnCount(2)
        self.form.tableWidget_transConfig.setHorizontalHeaderLabels(["Tx", "Rx"])
        
        # set column widths
        self.form.tableWidget_transConfig.horizontalHeader().setStretchLastSection(True)
        #self.form.tableWidget_transConfig.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        
        self.form.tableWidget_transConfig.show()

    def addTableItem(self, txList, rxList):
        # insert row at last position
        rowPosition = self.form.tableWidget_transConfig.rowCount()
        self.form.tableWidget_transConfig.insertRow(rowPosition)
        
        # set row with tx and rx
        self.form.tableWidget_transConfig.setItem(rowPosition,0,QTableWidgetItem(txList))
        self.form.tableWidget_transConfig.setItem(rowPosition,1,QTableWidgetItem(rxList))
        
    def addEmptyRow(self):
        self.addTableItem("","")