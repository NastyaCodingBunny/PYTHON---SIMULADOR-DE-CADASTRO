
######## BY CODING BUNNY ########

######## YOUTUBE CHANNEL : https://www.youtube.com/channel/UC1kiCskqM7wVFA0Pye1uDgA ########

######## PACKAGE USED : PyQt5 ########

######## INSTALLATION COMMAND FOR PYTHON 3 : "pip3 install PyQt5" ########





from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 60, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 100, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 140, 181, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 180, 181, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 220, 181, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 91, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 260, 231, 161))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 450, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.create)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 450, 61, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 450, 61, 41))
        self.pushButton.setObjectName("pushButton_1")
        self.pushButton.clicked.connect(self.mount)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Simulador de cadastro by Coding Bunny", "Simulador de cadastro by Coding Bunny"))
        self.label.setText(_translate("MainWindow", "NOME "))
        self.label_2.setText(_translate("MainWindow", "IDADE "))
        self.label_3.setText(_translate("MainWindow", "ESTADO"))
        self.label_4.setText(_translate("MainWindow", "CIDADE"))
        self.label_5.setText(_translate("MainWindow", "EMAIL"))
        self.pushButton_2.setText(_translate("MainWindow", "GERAR"))
        self.pushButton_3.setText(_translate("MainWindow", "LIMPAR"))
        self.pushButton.setText(_translate("MainWindow", "MONTAR"))

    
    def mount(self, MainWindow ):
        self.textEdit.setText("NOME :  " +  self.lineEdit.text() + "\nIDADE:  "
                         + self.lineEdit_2.text() + "\nESTADO:  "
                         + self.lineEdit_3.text() + "   \nCIDADE:  " + self.lineEdit_4.text()
                         + "   \nEMAIL:  " + self.lineEdit_5.text())
    


    def delete(self, MainWindow):
        self.textEdit.clear()








    def create(self):
         filename = self.lineEdit.text()
         filetext = "NOME : " + self.lineEdit.text() + "\nIDADE : " + self.lineEdit_2.text() + "\nESTADO : " + self.lineEdit_3.text() + "\nCIDADE : " + self.lineEdit_4.text() + "\nEMAIl : " + self.lineEdit_5.text()        
         createfile = open(filename, 'w')
         createfile.write(filetext)
         createfile.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

